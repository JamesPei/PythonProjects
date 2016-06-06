#__author__ = 'James'
#-*-coding:utf-8-*-

from itertools import chain

def tr(G):
    GT = {}
    for u in G: GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

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

if __name__=='__main__':
    G={'s':('a','c','e'),'a':'b','c':('b','d','f'), 'e':'f', 'b':'t', 'd':'t', 'f':'t', 't':''}
    G={'s':('a','c'),'a':'b','c':('b','d'), 'b':'t', 'd':'t', 't':''}
    s='s'
    t='t'
    print paths(G,s,t)
    
