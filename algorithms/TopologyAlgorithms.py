#__author__ = 'James'
#-*-coding:utf-8-*-

    #朴素拓扑排序法，时间复杂度O(n**2)
def naive_topsort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i+1
    seq.insert(min_i, v)
    return seq

#有向无环图的拓扑排序,时间复杂度O(n)
def topsort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S

#具有分层功能的拓扑排序
def toposort_group(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    G1=deepcopy(G)
    Q=deque([u for u in G if count[u] == 0])    # 初始节点
    S = []
    pre = [u for u in G if count[u] == 0]       # 上一层节点
    t=[]
    tails=[]                                    # 最后一层节点
    while Q:
        if not pre:
            t.append(deepcopy(S))
            S=[]
            pre = [u for u in G1 if count[u] == 0]
        u = Q.popleft()
        pre.remove(u)
        S.append(u)
        if not G[u]:                            # 不存在子节点
            tails.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
        if u in G1.keys():G1.pop(u)
    t.append(tails)
    return t

#indegree0函数返回入度为0的顶点，并在v和e中删除它和它相邻的边，如果v列表中没有顶点了，就返回None，
#如果v列表中还有顶点但是找不到入度为0的顶点，说明有向图中有环，返回-1。topoSort函数不断取出有向图中
#入度为0的顶点，最后就是拓扑排序序列
def indegree0(v,e):
    if v==[]:
        return None
    tmp=v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp==[]:
        return -1

    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i]='toDel' #占位，之后删掉
    if e:
        eset=set(e)
        eset.remove('toDel')
        e[:]=list(eset)
    if v:
        for t in tmp:
            v.remove(t)
    return tmp

def topoSort(v,e):
    result=[]
    while True:
        nodes=indegree0(v,e)
        if nodes==None:
            break
        if nodes==-1:
            print('there\'s a circle.')
            return None
        result.extend(nodes)
    return result

if __name__=='__main__':
    # v=['a','b','c','d','e','f']
    # e=[('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('a','f'),('b','f'),('b','d'),('d','f')]
    v=['a','b','c','d','e']
    e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
    res=topoSort(v,e)
    print(res)

    # G={'a':('b','f'),'b':('c','d','f'),'c':('d'),'d':('e','f'),'e':('f'),'f':()}
    G={'a':('b','d'),'b':('c'),'c':(),'d':('c','e'),'e':('c')}
    res=topsort(G)
    print res
