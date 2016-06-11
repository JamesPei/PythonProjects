#__author__ = 'James'
#-*-coding:utf-8-*-

from itertools import chain
from collections import deque
from collections import defaultdict

inf = float('inf')

def tr(G):
    GT = {}
    for u in G: GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

#=======================二分图最大匹配问题===========================
# 通过增广路径算法来寻找双边最大匹配
def match(G,X,Y):                                           # maximum bipartite matching
    H = tr(G)                                               # the transposed graph
    S,T,M = set(X), set(Y), set()                           # unmatched left/right + match
    while S:                                                # still unmatched on the left
        s = S.pop()                                         # get one
        Q,P = {s},{}                                        # start a traversal from it
        while Q:                                            # discovered, unvisited
            u = Q.pop()                                     # visit one
            if u in T:                                      # Finished augmenting path?
                T.remove(u)                                 # u is now matched
                break                                       # and our traversal is done
            forw = (v for v in G[u] if (u,v) not in M)      # possible new edges
            back = (v for v in H[u] if (v,u) in M)          # cancellations
            for v in chain(forw, back):                     # along out- and in-edges
                if v in P: continue                         # already visited? Ignore
                P[v] = u                                    # traversal predecessor
                Q.add(v)                                    # new nodel discovered
        while u != s:                                       # augment: backtrack to s
            u, v = P[u], u                                  # shift one step
            if v in G[u]:                                   # forward edge?
                M.add((u, v))                               # new edge
            else:                                           # backward edge?
                M.remove((v, u))                            # cancellation
    return M                                                # matching--a set of edges

# 使用带标记的遍历来寻找增广路径，并对边不相交的路径进行计数
def paths(G, s, t):                                         # edge-disjoint path count
    H, M, count = tr(G), set(), 0                           # transpose, matching, result
    while True:                                             # until the function returns
        Q, P = {s},{}                                       # traversal queue + tree
        while Q:                                            # discovered, unvisited
            u = Q.pop()                                     # get one
            if u==t:                                        # augmenting path!
                count += 1                                  # that means one more path
                break                                       # end the traversal
            forw = (v for v in G[u] if (u,v) not in M)      # possible new edges
            back = (v for v in H[u] if (v,u) in M)          # cancellations
            for v in chain(forw, back):                     # along out- and in-edges
                if v in P: continue                         # already visited? Ignore
                P[v] = u                                    # traversal predecessor
                Q.add(v)                                    # new node discovered
        else:                                               # didn't reach t?
            return count                                    # we're done
        while u != s:                                       # augment: backtrack to s
            u, v = P[u], u                                  # shift one step
            if v in G[u]:                                   # forward edge?
                M.add((u,v))                                # new edge
            else:                                           # backward edge?
                M.remove((v, u))                            # cancellation

#===========================最大流问题=================================
# 通过BFS与标记法来寻找增广路径
def bfs_aug(G, H, s, t, f):
    P, Q, F = {s:None}, deque([s]),{s:inf}                  # tree, queue, flow label
    def label(inc):                                         # flow increase at v from u?
        if v in P or inc <= 0: return                       # seen? unreachable? Ignore
        F[v], P[v] = min(F[u], inc), u                      # max flow here ? from where?
        Q.append(v)                                         # Discovered -- visit later
    while Q:                                                # Discovered, unvisited
        u = Q.popleft()                                     # get one(FIFO)
        if  u==t: return P, F[t]                            # reached t? augmenting path
        for v in G[u]: label(G[u][v]-f[u,v])                # label along out-edges
        for v in H[u]: label(f[v,u])                        # label along in-edges
    return None, 0                                          # no argmenting path found

# Ford-Fulkerson算法（默认使用Edmonds-Karp算法)
def ford_fulkerson(G, s, t, aug=bfs_aug):                   # max flow from s to t
    H, f = tr(G), defaultdict(int)                          # transpose and flow
    while True:                                             # while we can improve things
        P,c = aug(G,H,s,t,f)                                # Aug.path and capacity/slack
        if c==0: return f                                   # no augm. path found? Done!
        u = t                                               # start augmentation
        while u != s:                                       # backtrack to s
            u,v = P[u], u                                   # shift one step
            if v in G[u]: f[u,v] += c                       # forward edge? add slack
            else:         f[v,u] -= c                       # backward edge? cancel slack

#===========================最小成本流问题============================
# Busacker-Gowen算法，使用Bellman-Ford算法作为增广算法
def busacker_gowen(G,W,s,t):                                # Min-cost max-flow
    def sp_aug(G,H,s,t,f):                                  # shortest path(Bellman-Ford)
        D,P,F = {s:0},{s:None},{s:inf, t:0}                 # Dist, preds and flow
        def label(inc, cst):                                # Label + relax, really
            if inc<=0:  return False                        # No flow increase? skip it
            d = D.get(u,inf) + cst                          # New possible aug. distance
            if d>=D.get(v, inf):return False                # No improvement? skip it
            D[v],P[v] = d, u                                # Update dist and pred
            F[v] = min(F[u], inc)                           # Update flow label
            return True                                     # we changed things
        for _ in G:                                         # n=len(G) rounds
            changed = False                                 # No changes in round so far
            for u in G:                                     # Every from-node
                for v in G[u]:                              # Every forward to-node
                    changed |= label(G[u][v]-f[u,v],W[u,v]) # 按位或运算符：a|=2等价于a=a|2
                for v in H[u]:                              # Every backward to-node
                    changed |= label(f[v,u], -W[v,u])
            if not changed: break                           # No change in round: Done
        else:                                               # Not done before round n?
            raise ValueError('negative cycle')              # Negative cycle detected
        return P,F[t]                                       # Preds and flow reaching t
    return ford_fulkerson(G,s,t,sp_aug)                     # Max-flow with Bellman-Ford

if __name__=='__main__':
    # G={'s':('a','c'),'a':'b','c':('b','d'), 'b':'t', 'd':'t', 't':''}
    # s='s'
    # t='t'
    # print paths(G,s,t)

    G={'s':{'a':1,'c':2},'a':{'b':1},'c':{'b':2,'d':1}, 'b':{'t':2}, 'd':{'t':1}, 't':{}}
    print ford_fulkerson(G,'s','t')
