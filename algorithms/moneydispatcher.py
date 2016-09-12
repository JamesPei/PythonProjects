def money_dispatch(n):
    arr = [1,5,10,20,50,100]
    len =arr.__len__()
    res = [[None for j in range(1,n+2)] for i in range(len+1)]
    for i in range(len+1):
        res[i][0]=1
    for j in range(1,n+1):
        res[0][j]=0
    print res
    for i in range(1,len+1):
        for j in range(1,n+1):
            res[i][j]=0
            for k in range(j/arr[i-1]+1):
                # print k
                res[i][j]+=res[i-1][j-k*arr[i-1]]
    return res[len][n]

if __name__=='__main__':
    print money_dispatch(20)
