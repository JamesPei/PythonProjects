#__author__ = 'James'
#-*-coding:utf-8-*-

from string import ascii_lowercase as chars
from functools import wraps
from heapq import heappush,heappop

#记忆体化的装饰器函数
def memo(func):
    cache={}
    @wraps(func)    # make warp look like func
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

# 松弛技术
inf = float('inf')
def relax(W,u,v,D,P):
    d = D.get(u,inf)+W[u][v]
    if d < D.get(v, inf):
        D[v],P[v] = d, u
        return True

# Bellman-Ford算法
def bellman_ford(G,s):
    D,P = {s:0},{}                                                  # zero-dist to s; no parents
    for rnd in G:                                                   # n=len(G) rounds
        changed = False                                             # No changes in round so far
        for u in G:                                                 # for every from-node...
            for v in G[u]:                                          # ...and its to-nodes
                if relax(G,u,v,D,P):                                 # shoutcut to v from u?
                    changed = True                                   # yes, so something changed
        if not changed: break                                       # No change in round:Done
    else: raise ValueError('negative cycle')
    return D,P

# Dijkstra算法,运行时间Q((m+n)lgn):m边数，n:节点数
def dijkstra(G, s):
    D,P,Q,S = {s:0},{},[(0,s)],set()                                # Est., tree, queue, visited
    while Q:                                                       # Still unprocessed nodes?
        _, u = heappop(Q)                                           # Node with lowest estimate
        if u in S: continue                                       # already visited? skip it
        S.add(u)                                                    # we've visited it now
        for v in G[u]:                                             # go through all its negihbors
            relax(G,u,v,D,P)                                        # relax the out-edge
            heappush(Q, (D[v],v))                                   # add to queue, west as pri
    return D,P

# Johnson算法，适用于求解稀疏图(边相对较少的图),运行时间Q(mnlgn),是Dijkstra算法的n倍
from copy import deepcopy
def johnson(G):         # all pairs shortest paths
    G = deepcopy(G)      # dont want to break original
    s = object()         # Guaranteed unused node
    G[s] = {v:0 for v in G}     # edges from s have zero wgt
    h, _ = bellman_ford(G,s)     # h[v]:Shortest dist from s
    del G[s]                    # no more need for s
    for u in G:                 # the weight from u
        for v in G[u]:          # ...to v ...
            G[u][v] += h[u]-h[v]    # ...is adjusted(nonneg.)
    D,P = {},{}                     # D[u][v] and P[u][v]
    for u in G:                    # from every u...
        D[u],P[u] = dijkstra(G,u)   # find the shortest paths
        for v in G:                 # for each destination...
            D[u][v] += h[v]-h[u]    # ...readjust the distance
    return D,P                      # these are two-dimensional

# Floyd-Warshall算法的缓存式递归实现
def rec_floyd_warshall(G):                    # all shortest paths
    @memo                                        # store subsolutions
    def d(u,v,k):                                # u to v via 1...k
        if k==0: return G[u][v]                 # assumes v in G[u]
        return min(d(u,v,k-1), d(u,k,k-1)+d(k,v,k-1))           # use k or not?
    return {(u,v): d(u,v,len(G)) for u in G for v in G}       # D[u,v]=d(u,v,n)

# Floyd-Warshall算法，仅考虑距离
def floyd_warshall(G):
    D = deepcopy(G)         # no intermediates yet
    for k in G:            # look for shortcuts with k
        for u in G:
            for v in G:
                D[u][v] = min(D[u][v], D[u][k]+D[k][v])
    return D

# Floyd-Warshall算法
def floyd_warshall(G):
    D,P = deepcopy(G),{}
    for u in G:
        for v in G:
            if u==v or G[u][v]==inf:
                P[u,v] = None
            else:
                P[u,v] = u
    for k in G:
        for u in G:
            for v in G:
                shortcut = D[u][k] + D[k][v]
                if shortcut < D[u][v]:
                    D[u][v] = shortcut
                    P[u,v] = P[k,v]
    return D,P

# Dijkstra算法作为解决方案生成器的实现
def idijkstra(G,s):
    Q,S = [(0,s)],set()
    while Q:
        d,u = heappop(Q)
        if u in S: continue
        S.add(u)
        yield u,d
        for v in G[u]:
            heappush(Q, (d+G[u][v], v))

# Dijkstra双向图版本
from itertools import cycle
def bidir_dijkstra(G, s, t):
    Ds, Dt = {},{}                 # D from s and t, respectively
    forw, back = idijkstra(G, s), idijkstra(G,t)
    dirs = (Ds, Dt, forw), (Dt, Ds, back)       # alternating situations
    try:                                        # until one of forw/back ends
        for D, other, step in cycle(dirs):      # switch between the two
            v,d = next(step)                    # next node/distance for one
            D[v] = d                            # remember the distance
            if v in other: break               # also visited by the other
    except StopIteration: return inf           # one ran out before they met
    m = inf                                     # they met, now find the  path
    for u in Ds:                                # for every visited forw-node
        for v in G[u]:                          # ...go through its neighbors
            if not v in Dt: continue           # is it also back-visited?
            m = min(m, Ds[u]+G[u][v]+Dt[v])     # is this path better
    return m                                    # return the best path

# A*算法
def a_star(G, s, t, h):
    P,Q = {}, [(h(s), None, s)]
    while Q:
        d, p, u  = heappop(Q)                   # Node with lowest heuristic
        if u in P: continue                     # already visited? skip it
        P[u] = p                                # set path predecessor
        if u==t: return d-h(t),P
        for v in G[u]:
            w = G[u][v] - h(u) + h(v)           # modify weight wrt heuristic
            heappush(Q, (d+w, u, v))            # add to queue
    return inf, None

# 单词梯路径的隐式图
def variants(wd, words):                        # yield all word variants
    wasl = list(wd)
    for i,c in enumerate(wasl):
        for oc in chars:
            if c==oc: continue                  # dont replace with the same
            wasl[i]=oc                          # replace the character
            ow = ''.join(wasl)                  # make a string of the word
            if ow in words:                     # is it a valid word
                yield ow                        # then we yield it
        wasl[i] = c                             # reset teh character

class WordSpace:
    def __init__(self, words):
        self.words = words
        self.M = dict()

    def __getitem__(self, wd):
        if wd not in self.M:
            self.M[wd] = dict.fromkeys(variants(wd, self.words), 1)
        return self.M[wd]

    def heuristic(self, u, v):                  # the default heuristic
        return sum(a!=b for a,b in zip(u,v))    # how many characters differ?

    def ladder(self, s, t, h=None):             # utility wrapper for a_star
        if h is None:                           # allows other heuristics
            def h(v):
                return self.heuristic(v,t)
        _,P = a_star(self, s, t, h)             # get the predecessor map
        if P is None:
            return [s, None, t]                 # when no path exists
        u, p = t, []
        while u is not None:                    # walk backward from t
            p.append(u)                         # append every predecessor
            u = P[u]                            # take another step
        p.reverse()                             # the path is backward
        return p

if __name__=='__main__':
    a,b,c,d,e,f,g,h = range(8)
    G={
        a:{b:2, c:1, d:3, e:9, f:4},
        b:{c:4, e:3},
        c:{d:8},
        d:{e:7},
        e:{f:5},
        f:{c:2, g:2, h:2},
        g:{f:1, h:6},
        h:{f:9, g:8}
    }
    # G = {
    #     a: {b: 3, c: 7, d: 3, e: 9, f: 4},
    #     b: {c: 4, e: 3},
    #     c: {d: -4},
    #     d: {e: 7},
    #     e: {f: 5},
    #     f: {c: 2, g: 2, h: 2},
    #     g: {f: 1, h: 6},
    #     h: {f: 9, g: 8}
    # }
    # G={
    #     a:{b:2, c:1, d:3, e:9, f:4},
    #     b:{c:4, e:3},
    #     c:{d:8},
    #     d:{e:7},
    #     e:{f:5},
    #     f:{c:2, g:2, h:2},
    #     g:{f:1, h:-9},
    #     h:{f:9, g:8}
    # }
    print bellman_ford(G, a)
    # print dijkstra(G,a)
    # for i in idijkstra(G,a):
    #     print i
    # G={
    #     a:{b:2, c:1, d:3, e:9, f:4},
    #     b:{a:2, c:4, e:3},
    #     c:{a:1, b:4, d:8, f:2},
    #     d:{a:3, c:8, e:7},
    #     e:{a:9, b:3, d:7, f:5},
    #     f:{a:4, c:2, e:5, g:2, h:2},
    #     g:{f:2, h:6},
    #     h:{f:2, g:6}
    # }
    # print bidir_dijkstra(G,a,h)
    # a = variants('lead','gold')
