def getPointOfwords(n,m,aListRem,aListAll):
    aListRemSet=set(aListRem)
    aListAllSet=set(aListAll)
    point=0
    for item in aListRemSet:
        if item in aListAllSet:
            point=point+(len(item))**2

    return point

xinput=list(map(int,input().split()))
n,m=xinput[0],xinput[1]
aListRem=input().split()
aListAll=input().split()

print(getPointOfwords(n,m,aListRem,aListAll))
            
