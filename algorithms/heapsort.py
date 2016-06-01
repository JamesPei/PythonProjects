#__author__ = 'James'
#-*-coding:utf-8-*-

def sift_up(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos-1) >> 1
        parent = heap[parentpos]
        if parent <= newitem: break
        heap[pos] = parent
        pos = parentpos
    heap[pos] = newitem