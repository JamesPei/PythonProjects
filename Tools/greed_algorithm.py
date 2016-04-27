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

if __name__ == '__main__':
    seq = "abcdefghi"
    frq = [4,5,6,9,11,12,15,16,20]
    print huffman(seq, frq)



