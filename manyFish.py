# input()和input() 之间是由回车分界的
def getFishKind(minSize,maxSize,nfish,fishSize):

    fishKind=0
    
    for i in range(minSize,maxSize+1):
        for j in range(nfish):
            if 2<= i/fishSize[j] <=10 or 2<= fishSize[j]/i <=10:
                break
            if j==nfish-1:
                fishKind=fishKind+1
            #print(i,j,fishSize[j],fishKind)
        #print(i)
    return fishKind

sizeRange=input().split(' ')
nfish=int(input())
xfishSize=input().split(' ')
fishSize=list(map(int,xfishSize))

minSize,maxSize= int(sizeRange[0]),int(sizeRange[1])
fishKind=getFishKind(minSize,maxSize,nfish,fishSize)
print(fishKind)

    
        
