#__author__ = 'James'
#-*-coding:utf-8-*-

visited={}
def maxmatch(G, X, Y):
    match=0
    for i in X:
        for v in Y:
            if v in G[i] and v in visited.keys() and not visited[v]:
                visited[v]=1
                match+=1
                break
            elif v not in G[i] or v in visited.keys() and visited[v]:
                continue
            elif v not in visited.keys():
                visited[v]=1
                match+=1
                break
    return match

if __name__=='__main__':
    # G={'A':('1','3'), 'B':('2','4'), 'C':('1','4'), 'D':'3', '1':('A','C'), '2':'B', '3':('A','D'), '4':('B','C')}
    # G={'A':'1', 'B':'4', 'C':'4', 'D':'2', '1':'A', '2':'D', '4':('B','C')}
    # X=['A','B','C','D']
    # Y=['1','2','3','4']
    # G={'A':('1','3','6'), 'B':('2','3','4'), 'C':('7','4'), 'D':'7', 'E':('3','7'), 'F':('5','6'),'G':('4','6'),
    #    '1':'A', '2':'B', '3':('A','B', 'E'), '4':('B','C','G'), '5':'F', '6':('A','F','G'), '7':('C','D','E')}
    G={'A':'2', 'B':'2', 'C':'2', 'D':('3','4'), 'E':'3', 'F':'4','G':('5','7'),
       '1':'', '2':('A','B','C'), '3':('D', 'E'), '4':('D','F'), '5':'G', '6':'', '7':'G'}
    X=['A','B','C','D','E','F','G']
    Y=['1','2','3','4','5','6','7']
    print maxmatch(G,X,Y)
