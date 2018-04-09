# 分饼干  2x32x2

def getDistCookie(str,n):

    distKinds=0
    xNum=0
    strLen=len(str)
    
    rightList=[]
    reminder=0
    for i in range(strLen):            
        nRight=10**(strLen-i-1)  
        if str[i]=="X":
            xNum=xNum+1
            rightList.append(nRight)
        else:
            reminder=(reminder+int(str[i])*nRight)%n
 
    aList=[0]
    for i in range(xNum):    
        tempList=aList
        aList=[]
        for item in tempList:            
            for j in range(10):
                xitem=(reminder+item+j*rightList[i])%reminder
                aList.append(xitem)
                if i==xNum-1 and xitem%n==0:
                    distKinds=distKinds+1
    return distKinds

str=input()
n=int(input())
print(getDistCookie(str,n))
