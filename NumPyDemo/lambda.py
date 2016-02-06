#__author__ = 'James'
#-*-coding:utf-8-*-

#lambda的一般形式是关键字lambda后面跟一个或多个参数，紧跟一个冒号，
# 以后是一个表达式。lambda是一个表达式而不是一个语句。它能够出现在
# Python语法不允许def出现的地方。作为表达式，lambda返回一个值
# （即一个新的函数）。lambda用来编写简单的函数，而def用来处理更强大的任务。

import time

# f = lambda x,y,z : x+y+z
# print f(1,2,3)
#
# g = lambda x,y=2,z=3 : x+y+z
# print g(1,z=4,y=5)
#
# L = [(lambda x: x**2),
# 	(lambda x: x**3),
# 	(lambda x: x**4)]
# print L[0](2),L[1](2),L[2](2)
#
# D = {'f1':(lambda: 2+3),
# 	'f2':(lambda: 2*3),
# 	'f3':(lambda: 2**3)}
# print D['f1'](),D['f2'](),D['f3']()

#map函数可以在序列中映射函数进行操作。例如：
# def inc(x):
# 	return x+10
#
# L = [1,2,3,4]
# print map(inc,L)
#
# print map((lambda x: x+10),L)

#列表解析可以实现map函数同样的功能，而且往往比map要快。例如：
# time1 = time.time()
# print [x**2 for x in range(1000)]
# print time.time()-time1
# time2 = time.time()
# print map((lambda x: x**2), range(1000))
# print time.time()-time2

#列表解析比map更强大。例如：
# print [x+y for x in range(5) if x%2 == 0 for y in range(10) if y%2 ==1]

#生成器函数就像一般的函数，但它们被用作实现迭代协议，因此生成器函数只能在迭代语境中出现。例如：
# def gensquares(N):
# 	for i in range(N):
# 		yield i**2
#
# for i in gensquares(5):
# 	print i,

#所有的迭代内容（包括for循环、map调用、列表解析等等）将会自动调用iter函数，来看看是不是支持了迭代协议。
#生成器表达式就像列表解析一样，但它们是扩在圆括号()中而不是方括号[]中。例如：
# for num in (x**2 for x in range(5)):
# 	print num,

#列表解析比for循环具有更好的性能。尽管如此，在编写Python代码时，性能不应该是最优先考虑的
#没有return语句时，函数将返回None对象

