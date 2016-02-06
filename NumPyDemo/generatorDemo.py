#__author__ = 'James'
#-*-coding:utf-8-*-

import math
import Queue

# def gen():
#     for x in xrange(4):
#         tmp = yield x
#         if tmp == 'hello':
#             print 'world'
#         else:
#             print str(tmp)

# g = gen()   #gen()并不是函数调用，而是产生生成器对象。
#
# print g.next()
# print g.next()  #上一次调用next,执行到yield 0暂停，再次执行恢复环境，给tmp赋值(注意：这里的tmp的值并不是x的值，而是通过send方法接受的值)，由于我们没有调用send方法，所以
#                  #tmp的值为None,此时输出None，并执行到下一次yield x,所以又输出1.next()等价于send(None)
#
# print g.send('hello')

# def stop_immediately(name):
#     if name == 'skycrab':
#         yield 'okok'
#     else:
#         print 'nono'
#
# s=stop_immediately('sky')
# s.next()

# def print_successive_primes(iterations, base=10):
#     # 像普通函数一样，生成器函数可以接受一个参数
#
#     prime_generator = get_primes(base)
#
#     #看一下prime_generator.send(None)这一行，当你用send来“启动”一个生成器时（就是从生成器函数的第一行代码执行到第一个yield语句的位置），
#     # 你必须发送None。这不难理解，根据刚才的描述，生成器还没有走到第一个yield语句，如果我们发生一个真实的值，这时是没有人去“接收”它的。
#     # 一旦生成器启动了，我们就可以像上面那样发送数据了。
#     print prime_generator.send(None)
#     #prime_generator.next() 亦可
#
#     for power in range(iterations):
#         print(str(power)+':'+str(prime_generator.send(base ** power)))
#
# def get_primes(number):
#     while True:
#         if is_prime(number):
#             number = yield number   #像 other = yield foo 这样的语句的意思是，"返回foo的值，这个值返回给调用者的同时，将other的值也设置为那个值"
#         number+=1
#
# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3, int(math.sqrt(number) + 1), 2):
#             if number % current == 0:
#                 return False
#         return True
#     return False
#
# print_successive_primes(3)

# def tt():
#     for x in xrange(4):
#         print 'tt'+str(x)
#         yield
#
# def gg():
#     for x in xrange(4):
#         print 'xx'+str(x)
#         yield
#
# class Task():
#     def __init__(self):
#         self._queue = Queue.Queue()
#
#     def add(self,gen):
#         self._queue.put(gen)
#
#     def run(self):
#         while not self._queue.empty():
#             for i in xrange(self._queue.qsize()):
#                 try:
#                     gen= self._queue.get()  #get后队列长度减1
#                     gen.send(None)
#                 except StopIteration:
#                     pass
#                 else:
#                     self._queue.put(gen)
#
# t=Task()
# t.add(tt())
# t.add(gg())
# t.run()

import random

def get_data():
    """返回0到9之间的3个随机数"""
    return random.sample(range(10), 3)

def consume():
    """显示每次传入的整数列表的动态平均值"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """产生序列集合，传递给消费函数（consumer）"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing...')
        next(producer)
