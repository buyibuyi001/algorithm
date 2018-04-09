def getTimesOfEachNumberInPage1toN(n):
    
    if n<10:
        numTimesInPagelessthanTen = [0,0,0,0,0,0,0,0,0,0]
        for i in range(n):
                numTimesInPagelessthanTen[i+1]=1           
        return numTimesInPagelessthanTen
    
    #if n==10:
    #    return [1,2,1,1,1,1,1,1,1,1]
    
    else:

        nTemp=n
        numTimesInPageN = [0,0,0,0,0,0,0,0,0,0]
        while nTemp%10!=0 or nTemp//10!=0: 
            numTimesInPageN[nTemp%10]=numTimesInPageN[nTemp%10]+1   
            nTemp=nTemp//10
            
        alist=getTimesOfEachNumberInPage1toN(n-1)    
        for i in range(10):
            timesOfEachNumberInPages[i]=alist[i]+ numTimesInPageN[i]
                 
        return timesOfEachNumberInPages
    
numTimesInPageN = [0,0,0,0,0,0,0,0,0,0]   
timesOfEachNumberInPages = [0,0,0,0,0,0,0,0,0,0]
n=int(input())
print(getTimesOfEachNumberInPage1toN(n))



