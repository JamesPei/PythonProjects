#__author__ = 'James'
#-*-coding:utf-8-*-
from collections import Counter
from collections import defaultdict

class ArrangeAlgorithms():

    #寻找最大排列问题的递归算法思路的朴素实现方案,时间复杂度O(n**2)
    def naive_max_perm(self,M,A=None):
        if A==None:
            A = set(range(len(M)))
        if len(A)==1: return A
        B = set(M[i] for i in A)
        C = A-B
        if C:
            A.remove(C.pop())
            self.naive_max_perm(M,A)
        return A

    #寻找最大排列问题,时间复杂度O(n)
    def max_perm(self,M):
        n = len(M)
        A = set(range(n))
        count = [0]*n
        for i in M:
            count[i] += 1
        Q = [i for i in A if count[i]==0 ]
        while Q:
            i = Q.pop()
            A.remove(i)
            j = M[i]
            count[j] -= 1
            if count[j] == 0:
                Q.append(j)
        return A

    #排序算法
    def counting_sort(self, A, key=lambda x:x):
        B,C = [], defaultdict(list)     #output and counts
        for x in A:
            C[key(x)].append(x)         #count key(x)
        for k in range(min(C), max(C)+1):   #for every key in the range
            B.extend(C[k])                    #add values in sorted order
        return B

    #朴素版明星问题
    def naive_celeb(self, G):
        n = len(G)
        for u in range(n):               #for every candidate
            for v in range(n):           #for everyone else
                if u == v:  continue     #same person?Skip
                if G[u][v]: break        #candidate knows other
                if not G[v][u]: break    #other doesn't know candidate
            else:
                return u                   #no breaks?celebrate
        return None                        #couldn't find anyone



M = [2,2,0,5,3,5,7,4]
# print ArrangeAlgorithms().naive_max_perm(M)
# print ArrangeAlgorithms().max_perm(M)
print ArrangeAlgorithms().counting_sort(M)