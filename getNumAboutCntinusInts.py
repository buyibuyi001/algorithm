#input 函数会一次将所有输入以字符串方式返回，所以你要取信息就要自己处理
def getNumAboutContinueInts(n,alist):
    '''
    test case:
    5
    10 7 12 8 11
    '''
    if alist==[]:
        print ("mistake")
        return 0

    min=max=alist[0]
    sum=0
    for i in alist:
        if min>=i:
            min=i
        if max<=i:
            max=i
        sum=sum+i
        #print (min,max,sum)

    sumRef=(max-min+1)*(max+min)/2
    if max-min>n:
        print ("mistake")

    if sum==sumRef:
        print (min-1,' ',max+1)
    else:
        print (int(sumRef-sum))
    return 0

n = list(map(int,input().split()))[0]
alist  = list(map(int,input().split()))   
getNumAboutContinueInts(n,alist)
