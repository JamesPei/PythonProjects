#__author__ = 'James'
#-*-coding:utf-8-*-

from functools import wraps
from TopologyAlgorithms import topsort

#记忆体化的装饰器函数
def memo(func):
    cache={}
    @wraps(func)    # make warp look like func
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

def fib(i): #斐波那契数列的指数级运算
    if i<2: return 1
    return fib(i-1) + fib(i-2)

# 运用递归，记忆体化的方式解决DAG的最短路径问题
def rec_dag_sp(W,s,t):      # shortest path from s to t
    @memo                    # Memoize f
    def d(u):               # Distance from u to t
        if u==t: return 0   # we are there!
        return min(W[u][v]+d(v) for v in W[u])  # best of every first step
    return d(s)             #apply to actual start node

# DAG最短路径问题的迭代方式算法
def dag_sp(W, s, t):
    d = {u:float('inf') for u in W}     # Distance estimates
    d[s]=0                                # start node: Zero distance
    for u in topsort(W):                 # in top_sorted order...
        if u==t: break                   # have we arrived?
        for v in W[u]:                   # for each out-edge...
            d[v] = min(d[v], d[u]+W[u][v])  # relax the edge
    return d[t]                          # distance to t (from s)

# print fib(100)  #指数级耗时过长或无法计算
fib = memo(fib)
print fib(100)

