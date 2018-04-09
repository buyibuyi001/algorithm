def maxSumOfSubarray(alist):

    if alist==[]:
        return 0
    alist_len=len(alist)
    curMax=finMax=curSum=alist[0]

    for i in range(1,alist_len):
        
            
        curMax=max(alist[i],max(curSum,curSum+alist[i]))
        finMax=max(finMax,curMax )

        if curSum+alist[i]<0:
            curSum=0
        else:
            curSum+=alist[i]
        

        

    return finMax

alist=[-111,-2,-3,0,1,4,-1,9]
res=maxSumOfSubarray(alist)
print (res)
