def absSum(a,b):
    return abs(a)+abs(b)

def getMinTime(n,tX,tY,gx,gy,walkTime,taxiTime):
        
    distance=absSum(gx,gy)
    minTime=distance*walkTime
    for i in range(n):
        #if absSum(tX[i],tY[i])>distance:
        #    break
        tmpMinTime=absSum(tX[i],tY[i])*walkTime+absSum(gx-tX[i],gy-tY[i])*taxiTime
        minTime=min(minTime,tmpMinTime)
    return minTime

n = list(map(int,input().split()))[0]
tX= list(map(int,input().split(' ')))
tY= list(map(int,input().split(' ')))
xinput=list(map(int,input().split(' ')))
gx= xinput[0]
gy= xinput[1]
xinput= list(map(int,input().split(' ')))
walkTime= xinput[0]
taxiTime= xinput[1]

res=getMinTime(n,tX,tY,gx,gy,walkTime,taxiTime)
print(res)
