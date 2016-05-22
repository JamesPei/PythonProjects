#__author__ = 'James'
#-*-coding:utf-8-*-

from functools import wraps
from TopologyAlgorithms import topsort
from bisect import bisect

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

# 用记忆体，递归方式解决最长递增子序列问题
def rec_list(seq):
    @memo
    def L(cur):                                     #　Longest ending at seq[cur]
        res = 1                                     # Length is at least 1
        for pre in range(cur):                      # potential predecessors
            if seq[pre] <= seq[cur]:                # A valid (smaller) predec
                res = max(res, 1+L(pre))            # can we improve the solution?
        return res
    return max(L(i) for i in range(len(seq)))       # the longest of them all

# 用基本迭代方法解决最长递归子序列问题
def basic_lis(seq):
    L=[1]*len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+L[pre])
    return max(L)

# 最长递增子序列问题
def lis(seq):                       # longest increasing subseq
    end=[]                          # End-values for all lengths
    for val in seq:                 # try every value, in order
        idx = bisect(end, val)      # bisect(end, val)查找该数值(val)将会插入的位置并返回，而不会插入。
        if idx==len(end): end.append(val)   # longest seq.extended
        else: end[idx] = val        # Prev. endpoint reduced
    return len(end)                 # the longest we found

# 用递归，记忆体化方式解决LCS问题
def rec_lcs(a,b):
    @memo
    def L(i,j):
        if min(i,j)<0: return 0
        if a[i]==b[j]: return 1+L(i-1, j-1)
        return max(L(i-1,j),L(i,j-1))
    return L(len(a)-1, len(b)-1)
# 迭代版LCS
def lcs(a,b):
    n,m = len(a),len(b)
    pre,cur=[0]*(n+1),[0]*(n+1)
    for j in range(1,m+1):
        pre,cur=cur,pre
        for i in range(1,n+1):
            if a[i-1]==b[j-1]:
                cur[i]=pre[i-1]+1
            else:
                cur[i]=max(pre[i], cur[i-1])
    return cur[n]

# 用递归，记忆体化方式解决无限制的整数背包问题，时间复杂度Θ（cn）伪多项式级
def rec_unbounded_knapsack(w,v,c):      #weights, values and capacity
    @memo
    def m(r):
        if r==0: return 0
        val = m(r-1)
        for i,wi in enumerate(w):
            if wi > r: continue
            val = max(val, v[i] + m(r-wi))
        return val
    return m(c)

# 迭代版无限制的整数背包问题，时间复杂度Θ（cn）伪多项式级
def unbounded_knapsack(w, v, c):
    m=[0]
    for r in range(1, c+1):
        val=m[r-1]
        for i,wi in enumerate(w):
            if wi>r: continue
            val = max(val, v[i]+m[r-wi])
        m.append(val)
    return m[c]

# 用递归，记忆体化方式解决0-1背包问题，时间复杂度Θ（cn）伪多项式级
def rec_knapsack(w, v, c):
    @memo
    def m(k, r):
        if k==0 or r==0 :return 0
        i = k-1
        drop = m(k-1, r)
        if w[i] > r: return drop
        return max(drop, v[i]+m(k-1, r-w[i]))
    return m(len(w), c)

# 迭代方式解决0-1背包问题，时间复杂度Θ（cn）伪多项式级
def knapsack(w, v, c):              # returns solution matrices
    n = len(w)                        # number of available items
    m = [[0]*(c+1) for i in range(n+1)]     # empty max-value matrix
    P = [[False]*(c+1) for i in range(n+1)] # empty keep/drop matrix
    for k in range(1, n+1):                 # we can use k first objects
        i = k-1                             # object under consideration
        for r in range(1, c+1):             # Every positive capacity
            m[k][r] = drop = m[k-1][r]      # by default: drop the  object
            if w[i] > r: continue          # too heavy? Ignore it
            keep = v[i] + m[k-1][r-w[i]]    # value  of keeping it
            m[k][r] = max(drop, keep)       # best of dropping and keeping
            P[k][r] = keep > drop           # did we keep it?
    return m, P                            # retrun full results

# 用于实现最优搜索树的记忆体化递归函数
def rec_opt_tree(p):
    @memo
    def s(i,j):
        if i==j: return 0
        return s(i,j-1)+p[j-1]
    @memo
    def e(i,j):
        if i==j: return 0
        sub = min(e(i,r)+e(r+1,j) for r in range(i,j))
        return sub + s(i,j)
    return e(0,len(p))

# 用迭代方式解决最优搜索树问题
from collections import defaultdict
def opt_tree(p):
    n = len(p)
    s,e = defaultdict(int), defaultdict(int)
    for k in range(1,n+1):
        for i in range(n-k+1):
            j = i+k
            s[i,j] = s[i,j-1] + p[j-1]
            e[i,j] = min(e[i,r]+e[r+1,j] for r in range(i,j))
            e[i,j] += s[i,j]
    return e[0,n]

if __name__=='__main__':
    # print fib(100)  #指数级耗时过长或无法计算

    # 利用记忆体化求斐波那契数列
    # fib = memo(fib)
    # print fib(100)

    dag={'a':{'b':2, 'f':9}, 'b':{'c':1, 'd':2, 'f':6}, 'c':{'d':7}, 'd':{'e':2, 'f':3}, 'e':{'f':4}, 'f':{}}
    # print rec_dag_sp(dag, 'a', 'f')
    # print dag_sp(dag, 'a', 'f')

    seq=[1,2,3,6,8,0,4,5,11,32,12]
    # print lis(seq)

    a,b='spock','asoka'
    # print rec_lcs(a,b)
    print lcs(a,b)
