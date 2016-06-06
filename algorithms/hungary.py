#__author__ = 'James'
#-*-coding:utf-8-*-

M=[]
class hungary():

    def __init__(self, nx, ny, edge, cx, cy, visited):
        self.nx, self.ny=nx, ny
        self.edge = edge
        self.cx, self.cy=cx,cy
        self.visited=visited

    def max_match(self):
        res=0
        self.cx={'A':-1,'B':-1,'C':-1}
        self.cy={'E':-1,'F':-1,'G':-1}

        for i in self.nx:
            if self.cx[i]==-1:
                self.visited={'E':0,'F':0,'G':0}
                res+=self.path(i)
        return res

    def path(self, u):
        for v in self.ny:
            if self.edge[u][v] and (not self.visited[v]):
                self.visited[v]=1
                print self.cy[v]
                if self.cy[v]==-1 or self.path(v):
                    self.cx[u] = v
                    self.cy[v] = u
                    M.append((u,v))
                    print M
                    return 1
        return 0

if __name__ == '__main__':
    nx, ny=['A','B','C'] ,['E','F','G']
    edge={'A':{'E':1,'F':1}, 'B':{'G':1}, 'C':{'E':1, 'G':1}}
    cx, cy={},{}
    visited={'E':0,'F':0,'G':0}
    print hungary(nx, ny, edge, cx, cy, visited).max_match()

