#__author__ = 'James'
#-*- coding:utf-8 -*-

from heapq import heapify, heappop, heappush
from itertools import count

#哈夫曼算法
def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))    # num ensures valid ordering
    heapify(trees)                        # a min-heap based on frq
    while len(trees) > 1:                # until all are combined
        fa, _, a = heappop(trees)         # get the two smallest trees
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))     # combine and re-add them
    return trees[0][-1]

#从哈夫曼树中提取出哈夫曼编码
def codes(tree, prefix=""):
    if len(tree) == 1:
        yield (tree, prefix)    #A leaf with its codes
        return
    for bit, child in zip("01", tree):
        for pair in codes(child, prefix + bit): #get codes recursively
            yield pair

#kruskal算法,时间复杂度(mlgn)
def find(C, u):
    if C[u] != u :
        C[u] = find(C, C[u])       # path compression
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)   #union by rank
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:        # A tie: Move v up a level
        R[v] += 1

def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R= {u:u for u in G}, {u:0 for u in G}    #Comp, reps and ranks
    for _, u, v in sorted(E):
        if find(C, u) != find(C,v):
            T.add((u, v))
            union(C, R, u, v)
    return T

#Prim算法
def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        # print 'Q:',Q
        _, m, u = heappop(Q)
        if u in P: continue
        P[u] = m
        # print 'P:',P
        for v,w in G[u].items():
            heappush(Q, (w, u, v))
    P = [(k,v) for k,v in P.items() if v!=None]
    return P

if __name__ == '__main__':
    # seq = "abcdefghi"
    # frq = [4,5,6,9,11,12,15,16,20]
    # print huffman(seq, frq)
    G={'A':{'D':5,'B':7}, 'B':{'A':7,'C':8,'E':7,'D':9},'C':{'B':8,'E':5},'D':{'A':5,'B':9,'E':15,'F':6},'E':{'B':7,'C':5,'D':15,'F':8, 'G':9},
       'F':{'D':6, 'E':8, 'G':11}, 'G':{'E':9, 'F':11}}
    # G={'A':{'D':5,'B':7}, 'B':{'A':7,'C':8,'E':7,'D':9},'C':{'B':8,'E':5},'D':{'A':5,'B':9,'E':15},'E':{'B':7,'C':5,'D':15}}
    # print prim(G,'B')
    G1={'A':{'D':5,'B':7}, 'B':{'A':7,'C':8,'E':7,'D':9},'C':{'B':8,'E':5},'D':{'A':5,'B':9,'E':15,'F':6},'E':{'B':7,'C':5,'D':15,'F':8, 'G':9},
       'F':{'D':6, 'E':8, 'G':11}, 'G':{'E':9, 'F':11}}
    print kruskal(G1)


