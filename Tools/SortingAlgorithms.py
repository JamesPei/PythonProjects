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

    #计数排序：假设n个输入元素中每一个都是介于0到k之间的整数，此处k为某个整数。当k=O(n)时，计数排序的运行时间为Θ(n)
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

    # 基数排序

    #约瑟夫出圈
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
