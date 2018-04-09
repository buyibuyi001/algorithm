#需要循环时，变量的初始化能在循环内完成的尽量循环内完成，这样看起来代码简单

def getShortestContiSubarray(number,length):
    
    if number<1 or number>1000000000 or length<2 or length>100:
        print('No')
        return 0
        
    for i in range(length,100):       
        nstart = max(number//i-i//2,1)        
        sum0=(nstart+nstart+i-1)*i/2
        
        if sum0==N:
            for j in range(nstart,nstart+i):
                if j != nstart+i-1:
                    print(j,end=' ')
                else:
                    print(j)
            
            return 0
        
        sum1=(nstart+1+nstart+i)*i/2
        if sum1==N:
            for j in range(nstart+1,nstart+i+1):
                if j != nstart+i-1:
                    print(j,end=' ')
                else:
                    print(j)
            return 0

xinput=list(map(int,input().split(' ')))
N,L=xinput[0],xinput[1]
getShortestContiSubarray(N,L)


