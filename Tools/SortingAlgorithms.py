#__author__ = 'James'
#-*- coding:utf-8 -*-
import random

class SortingAlgorithms:

    #侏儒排序：时间复杂度Ω（n)到O(n**2)
    def gnomesort(self,seq):
        i=0
        while i < len(seq):
            if i == 0 or seq[i-1] <= seq[i]:
                i += 1
            else:
                seq[i],seq[i-1] = seq[i-1],seq[i]
                i -= 1
        return seq

    #归并排序：时间复杂度Θ（nlgn）
    def mergesort(self, seq):
        mid = len(seq)//2
        lft, rgt = seq[:mid],seq[mid:]
        if len(lft) > 1: lft = self.mergesort(lft)
        if len(rgt) > 1: rgt = self.mergesort(rgt)
        res = []
        while lft and rgt:
            if lft[-1] >= rgt[-1]:
                res.append(lft.pop())
            else:
                res.append(rgt.pop())
        res.reverse()
        return (lft or rgt) + res

    #计数排序：当输入的元素是 n 个 0 到 k 之间的整数时，时间复杂度是 Θ(n + k)
    #http://www.knowsky.com/884995.html
    def countingSort(self, alist, k):
        n = len(alist)
        b = [0 for i in xrange(n)]
        c = [0 for i in xrange(k+1)]
        for i in alist:
            c[i] += 1
        for i in xrange(1, len(c)):
            c[i] = c[i-1] + c[i]
        for i in alist:
            b[c[i]-1] = i
            c[i] -= 1
        return b

    # 对于N个待排数据，M个桶，平均每个桶[N/M]个数据的桶排序平均时间复杂度为：O(N+N*logN-N*logM)
    # 当N=M时，即极限情况下每个桶只有一个数据时。桶排序的最好效率能够达到O(N)
    # 桶排序的缺点：空间复杂度大,即内存占用大
    def bucketSort(self, oldlist):
        _max=oldlist[0]     #数组中最大值
        for i in oldlist:
            if i>_max:
                _max=i
        _min=oldlist[0]     #数组中最小值
        for i in oldlist:
            if i<_min:
                _min=i

        s=[0 for i in xrange(_min,_max+1)]
        for i in oldlist:
            s[i-_min]+=1
        current=_min
        n=0
        for i in s:
            while i>0:
                oldlist[n]=current
                i-=1
                n+=1
            current+=1

    # 区间[0,1)均匀分布的桶排序
    def sort(self,a):
        n=len(a)
        s=[[] for i in xrange(n)]
        for i in a:
            s[int(i*n)].append(i)
        for i in s: #分别对每个桶进行排序
            self.insertSort(i)
        return [i for j in s for i in j]

    def insertSort(self,a):
        n=len(a)
        if n<=1:
            pass
        for i in range(1,n):    # O(n)级排序
            key=a[i]
            j=i-1
            while key<a[j] and j>=0:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key

    #基数排序
    def radixSort(self):
        A = [random.randint(1, 9999) for i in xrange(10000)]
        for k in xrange(4): #四轮排序
            s = [[] for i in xrange(10)]
            for i in A:
                s[i/(10**k)%10].append(i)
            A = [a for b in s for a in b]
        return A


    #出圈问题
    def leavecircle(self, total, num):
        a = [i+1 for i in range(total)]
        i = 0
        j = 1
        length = len(a)
        while(length>0):
            if(a[i%total] > 0):
                if(j == num):
                    print a[i%total]
                    a[i%total] = -1
                    j = 1
                    i += 1
                else:
                    j += 1
                    i += 1
            else:
                i += 1

# a = SortingAlgorithms().gnomesort([1,8,5,7,3,2,0,9,4,6,34,12,55,29])
# b = SortingAlgorithms().mergesort([1,8,5,7,3,2,0,9,4,6,34,12,55,29])
# print  a
# print  b
# print SortingAlgorithms().leavecircle(10,3)

print SortingAlgorithms().countingSort([random.randint(0,100) for i in xrange(100)], 100)
