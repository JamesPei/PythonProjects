#__author__ = 'James'
#-*-coding:utf-8-*-

M=[]
class DFS_hungary():

    def __init__(self, nx, ny, edge, cx, cy, visited):
        self.nx, self.ny=nx, ny
        self.edge = edge
        self.cx, self.cy=cx,cy
        self.visited=visited

    def max_match(self):
        res=0
        for i in self.nx:
            if self.cx[i]==-1:
                # self.visited={'E': 0, 'F': 0, 'G': 0,'H':0}
                for key in self.ny:         # 将visited置0表示未访问过
                    self.visited[key]=0
                res+=self.path(i)
        print M
        return res

    def path(self, u):
        for v in self.ny:
            if self.edge[u][v] and (not self.visited[v]):
                self.visited[v]=1
                if self.cy[v]==-1:
                    self.cx[u] = v
                    self.cy[v] = u
                    M.append((u,v))
                    return 1
                else:
                    M.remove((self.cy[v], v))
                    if self.path(self.cy[v]):
                        self.cx[u] = v
                        self.cy[v] = u
                        M.append((u, v))
                        return 1
        return 0

class BFS_hungary():

    def max_match(self):
        res = 0
        Mx={'A':-1,'B':-1,'C':-1}
        My={'E':-1,'F':-1,'G':-1}
        g={'A':{'E':1,'F':1,'G':0}, 'B':{'E':0, 'F':0, 'G':1}, 'C':{'E':1, 'F':0, 'G':1}}
        visited={'E':-1,'F':-1,'G':-1}
        Q={}
        prev={}

        for i in Mx:
            if Mx[i]==-1:                           # 对于集合中的每一个没有匹配的点i进行一次bfs找交错轨
                qs = qe = 0
                Q[qe] = i
                qe += 1
                prev[i]=-1

                flag=0                              # 判断是否找到
                while(qs<qe and not flag):          # 确保回到最初
                    u = Q[qs]
                    for v in My:
                        if not flag:
                            if g[u][v] and visited[v]!=i:
                                visited[v]=i
                                Q[qe]=My[v]
                                qe += 1
                                if My[v]>=0:
                                    prev[My[v]] = u
                                else:
                                    flag=1
                                    d = u
                                    e = v
                                    while d!=-1:
                                        t = Mx[d]
                                        Mx[d] = e
                                        My[e] = d
                                        d = prev[d]
                                        e = t
                            qs+=1
                if(Mx[i]!=-1):
                    res += 1
            return res

if __name__ == '__main__':
    # nx, ny=['A','B','C'] ,['E','F','G']
    # edge={'A':{'E':1,'F':1,'G':0}, 'B':{'E':0, 'F':0, 'G':1}, 'C':{'E':1, 'F':0, 'G':1}}
    # cx, cy={'A':-1,'B':-1,'C':-1},{'E':-1,'F':-1,'G':-1}
    # visited={'E':0,'F':0,'G':0}
    # # nx, ny = ['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H']
    # # edge = {'A':{'E': 1, 'F': 0, 'G': 1, 'H':0}, 'B':{'E': 0, 'F': 1, 'G': 0, 'H':1}, 'C':{'E': 1, 'F': 0, 'G': 0, 'H':1}, 'D':{'E': 0, 'F': 0, 'G': 1, 'H':0}}
    # # cx, cy = {'A':-1,'B':-1,'C':-1,'D':-1}, {'E':-1,'F':-1,'G':-1,'H':-1}
    # # visited = {'E': 0, 'F': 0, 'G': 0,'H':0}
    #
    # # dfs算法寻找增广路，常用在稠密图中，算法的复杂度为O(n3)
    # print DFS_hungary(nx, ny, edge, cx, cy, visited).max_match()

    print BFS_hungary().max_match()