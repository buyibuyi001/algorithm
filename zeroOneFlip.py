def zeroOneFlip(nZero,nOne,nCount):
    if nZero+nOne<nCount:
        return -1
    if nZero%nCount==0:
        return nZero//nCount

    minTimes=0
    while true:
        j=1
        for i in range(1,nCount+1):
            if i==nCount-i:
                continue
            if nOne-(nCount-2*i)*j>0:
                if nZero+(nCount-2*i)*j==nCount:
                    return
        j=j+1


xinput=list(map(int,input().split()))
nZero,nOne,nCount=xinput[0],xinput[1],xinput[2]

res=zeroOneFlip(nZero,nOne,nCount)
print (res)
