#__author__ = 'James'
#-*-coding:utf-8-*-

# https://docs.python.org/2/library/multiprocessing.html?highlight=multiprocessing#module-multiprocessing

from multiprocessing import Pool
from multiprocessing import Process,Queue,Pipe,Lock,Value,Array,Manager
import os

def f(x):
    return x*x

def f1(name):
    print 'hello,',name

def info(title):
    print title
    print 'module name:',__name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f2(name):
    info('function f2')
    print 'hello,',name

def f3(q):
    q.put([42, None, 'hello'])

def f4(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def f5(l, i):
    l.acquire()
    print 'hello world', i
    l.release()

def f6(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def f7(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    # p = Pool(5)
    # print(p.map(f, [1, 2, 3]))

    # p=Process(target=f1, args=('James',))
    # p.start()
    # p.join()

    # info('main line')
    # p = Process(target=f2, args=('bob',))   #新建一个process,这个process将是main的子process
    # p.start()
    # p.join()

    # q = Queue()     # Queues are thread and process safe
    # p = Process(target=f3, args=(q,))
    # p.start()
    # print q.get()    # prints "[42, None, 'hello']"
    # p.join()

    #The Pipe() function returns a pair of connection objects
    # connected by a pipe which by default is duplex (two-way)
    # parent_conn, child_conn = Pipe()
    # p = Process(target=f4, args=(child_conn,))
    # p.start()
    # print parent_conn.recv()   # prints "[42, None, 'hello']"
    # p.join()

    # lock = Lock()
    # for num in range(50):
    #     Process(target=f5, args=(lock, num)).start()

    # num = Value('d', 0.0)
    # arr = Array('i', range(10))       # 'd' indicates a double precision float and 'i' indicates a signed integer.These shared objects will be process and thread-safe.
    # p = Process(target=f6, args=(num, arr))
    # p.start()
    # p.join()
    # print num.value
    # print arr[:]

    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p = Process(target=f7, args=(d, l))
    p.start()
    p.join()
    print d
    print l