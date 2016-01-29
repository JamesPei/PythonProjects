#__author__ = 'James'
#-*-coding:utf-8-*-

# def gen():
#     for x in xrange(4):
#         tmp = yield x
#         if tmp == 'hello':
#             print 'world'
#         else:
#             print str(tmp)
#
# g = gen()   #gen()并不是函数调用，而是产生生成器对象。
#
# print g.next()
# print g.next()  #上一次调用next,执行到yield 0暂停，再次执行恢复环境，给tmp赋值(注意：这里的tmp的值并不是x的值，而是通过send方法接受的值)，由于我们没有调用send方法，所以
#                  #tmp的值为None,此时输出None，并执行到下一次yield x,所以又输出1.next()等价于send(None)
#
# print g.send('hello')

def stop_immediately(name):
    if name == 'skycrab':
        yield 'okok'
    else:
        print 'nono'

s=stop_immediately('sky')
s.next()
