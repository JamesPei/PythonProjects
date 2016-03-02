#__author__ = 'James'
#-*-coding:utf-8-*-

import Queue

class Task():

    def __init__(self):
        self._queue = Queue.Queue()

    def add(self,gen):
        self._queue.put(gen)

    def run(self):
        while not self._queue.empty():
            print 'self._queue is not empty'
            print 'self._queue.qsize:',self._queue.qsize()
            for i in xrange(self._queue.qsize()):
                print 'i:',i
                try:
                    gen = self._queue.get()
                    gen.send(None)
                    # print gen.next()
                except  StopIteration:
                    pass
                else:
                    self._queue.put(gen)

def tt():
    for x in xrange(4):
        print 'tt'+str(x)
        yield

def gg():
    for x in xrange(4):
        print 'gg'+str(x)
        yield

t=Task()
t.add(tt())
t.add(gg())
t.run()