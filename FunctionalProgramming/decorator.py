#__author__ = 'James'
#-*-coding:utf-8-*-

#使用内嵌包装函数来确保每次新函数都被调用，内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'

#对带参数的函数进行装饰，内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
def deco1(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret  # return or not looks no difference
    return _deco

@deco1
def myfunc1(a, b):
    print(" myfunc1(%s,%s) called." % (a, b))
    return a + b

# 对参数数量不确定的函数进行装饰，参数用(*args, **kwargs)，自动适应变参和命名参数
def deco2(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco2
def myfunc2(a, b):
    print(" myfunc2(%s,%s) called." % (a, b))
    return a+b

@deco2
def myfunc3(a, b, c):
    print(" myfunc3(%s,%s,%s) called." % (a, b, c))
    return a+b+c

#让装饰器带参数
def deco3(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco3("mymodule")
def myfunc4():
    print(" myfunc() called.")

@deco3("module2")
def myfunc5():
    print(" myfunc2() called.")


# myfunc()

# myfunc1(1,2)

# myfunc2(1, 2)
# myfunc3(1, 2, 3)

