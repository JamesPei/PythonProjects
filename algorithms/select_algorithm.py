#__author__ = 'James'
#-*-coding:utf-8-*-

#划分与选取算法的一种简单实现
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k: return pi
    elif m<k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)

#快速排序
def quicksort(seq):
    if len(seq) <=1: return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

