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
            u, v = P[u], u                                   # shift one step
            if v in G[u]:                                   # forward edge?
                M.add((u, v))                               # new edge
            else:                                           # backward edge?
                M.remove((v, u))                             # cancellation
    return M                                                # matching--a set of edges

# 使用带标记的遍历来寻找增广路径，并对边不想交的路径进行计数
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

# 通过BFS与标记法来寻找增广路径
def bfs_aug(G, H, s, t, f):
    P, Q, F = {s:None}, deque([s]),{s:inf}      # tree, queue, flow label
    def label(inc):                             # flow increase at v from u?
        if v in P or inc <= 0: return          # seen? unreachable? Ignore
        F[v], P[v] = min(F[u], inc), u           # max flow here ? from where
        Q.append(v)
    while Q:
        u = Q.popleft()
        if  u==t: return P, F[t]
        for v in G[u]: label(G[u][v]-f[u,v])
        for v in H[u]: label(f[v,u])
    return None, 0

# Ford-Fulkerson算法（默认使用Edmonds-Karp算法)
def ford_fulkerson(G, s, t, aug=bfs_aug):
    H, f = tr(G), defaultdict(int)

if __name__=='__main__':
    # G={'A':('1','3'), 'B':('2','4'), 'C':('1','4'), 'D':'3', '1':('A','C'), '2':'B', '3':('A','D'), '4':('B','C')}
    # X=['A','B','C','D']
    # Y=['1','2','3','4']
    G={'A':('E','F'),'B':'G','C':('E','G'), 'E':('A','C'), 'F':'A', 'G':('B', 'C')}
    X=['A', 'B', 'C']
    Y=['E', 'F', 'G']
    M=match(G,X,Y)
    print M
    
