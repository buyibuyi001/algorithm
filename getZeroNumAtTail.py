# 不写return 会返回None
def getZeroNum(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    zeroNum=0
    while product%10==0:
        zeroNum=zeroNum+1
        product=product//10
    return zeroNum
        

n=int(input())
print(getZeroNum(n))
