# 求集合元素个数

def getNumOfSet(xinput):
    w,x,y,z=xinput[0],xinput[1],xinput[2],xinput[3]
    aSet=set()
    for i in range(w,x+1):

        for j in range(y,z+1):
            aSet.add(i/j)
            

    #numOfSet=0

    return len(aSet)
    

xinput=list(map(int,input().split()))
print(getNumOfSet(xinput))
