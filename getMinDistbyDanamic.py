def getMinDist(n,alist):
    preDist,curDist=0,0
    distSum=abs(alist[1]-alist[0])
    iflag=2
    maxDistSum=abs(alist[1]-alist[0])+abs(alist[2]-alist[1])
    
    for i in range(2,n):
        preDist=abs(alist[i-1]-alist[i-2])
        curDist=abs(alist[i]-alist[i-1])
        if maxDistSum<preDist+curDist:
            maxDistSum=preDist+curDist
            iflag=i
        distSum=distSum+curDist
    addDist=abs(alist[iflag]-alist[iflag-2])

    return distSum-maxDistSum+addDist

n=int(input())
alist=list(map(int,input().split()))
res=getMinDist(n,alist)
print(res)
