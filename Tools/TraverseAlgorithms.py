#__author__ = 'James'
#-*-coding:utf-8-*-

from collections import deque

#遍历一个表示为邻接集的图结构的连通分量
def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

#找出图的连通分量,找出图的连通分量是一个Θ(E+V)的操作
def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen: continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp

#递归版的深度优先搜索
def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)

#迭代版深度优先搜索
def iter_dfs(G, s):
    S,Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        Q.extend(G[u])
        yield u

#通用性的图遍历函数
def traverse(G, s, qtype=set):
    S,Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

#带时间戳的深度优先搜索
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()
    d[s] = t; t+=1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t; t+=1
    return t

#基于深度优先搜索的拓扑排序
def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

#迭代深度的深度优先搜索
def iddfs(G, s):
    yielded = set()
    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0: return
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G, u, d-1, S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded) == n: break
        for u in recurse(G, s, d):
            yield u

#广度优先搜索
def bfs(G, s):
    P, Q = {s:None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P

#Kosaraju查找强连通分量算法
def tr(G):
    GT = {}
    for u in G: GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs

G={0:{1,2,3,4,5},1:{0,2,4},2:{0,1,3,5},3:{0,2,4},4:{0,1,3,5},5:{0,2,4,6,7},6:{5,7},7:{5,6},8:{9,10},9:{8,10},10:{8,9}}
# G2 = {'a':('b','f'),'b':('c','d','f'),'c':('d'),'d':('e','f'),'e':('f'),'f':()}
# print components(G)
print walk(G, 1)
# rec_dfs(G,2)
# print list(iter_dfs(G,2))
# print dfs_topsort(G2)
