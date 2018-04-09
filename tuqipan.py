#涂棋盘
def getijMaxArea(i,j):

    ijFlag[i][j]=-1
    '''for k in range(4):
        x=i+next[k][0]
        y=j+next[k][1]
        getijMaxArea(x,y)'''

    if 0<i-1<n and array[i][j]==array[i-1][j] and ijFlag[i-1][j]!=-1:
        if ijAreaMax[i-1][j]==0:
            getijMaxArea(i-1,j)
        tmpijMaxArea=tmpijMaxArea+ijMaxArea(i-1,j)
    if 0<i+1<n and array[i][j]==array[i+1][j] and ijFlag[i+1][j]!=-1:
        if not ijAreaMax[i+1][j]:
            getijMaxArea(i+1,j)
        tmpijMaxArea=tmpijMaxArea+ijMaxArea[i+1][j]
    if 0<j-1<n and array[i][j]==array[i][j-1] and ijFlag[i][j-1]!=-1:
        if not ijAreaMax[i][j-1]:
            getijMaxArea(i,j-1)
        tmpijMaxArea=tmpijMaxArea+ijMaxArea[i][j-1]
    if 0<j+1<n and array[i][j]==array[i][j+1] and ijFlag[i][j+1]!=-1:
        if not ijAreaMax[i][j+1]:
            getijMaxArea(i,j+1)
        tmpijMaxArea=tmpijMaxArea+ijMaxArea[i][j+1]

    ijMaxArea[i][j]==max(ijMaxArea[i][j] , tmpijMaxArea )
    tmpijMaxArea=1

    return 0


n=int(input())
array=[]
for i in range(n):
    array.append(input())

ijAreaMax=[[0 for i in range(n)]for i in range(n)]
ijFlag=[[0 for i in range(n)]for i in range(n)]

#print(ijAreaMax)

tmpijMaxArea=1,
for i in range(n):
       for j in range(n):
           getijMaxArea(i,j)
           maxArea=max(maxArea,ijMaxArea(i,j))

print (maxArea)
