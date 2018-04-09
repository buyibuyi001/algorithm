#涂棋盘
def getijMaxArea(i,j):
    
    ijFlag[i][j]='r'
    comArea.append((i,j))    
    if 0<i-1<n and array[i][j]==array[i-1][j] and ijFlag[i-1][j]!='r':        
        getijMaxArea(i-1,j)
    if 0<i+1<n and array[i][j]==array[i+1][j] and ijFlag[i+1][j]!='r':       
        getijMaxArea(i+1,j)        
    if 0<j-1<n and array[i][j]==array[i][j-1] and ijFlag[i][j-1]!='r':        
        getijMaxArea(i,j-1)
    if 0<j+1<n and array[i][j]==array[i][j+1] and ijFlag[i][j+1]!='r':        
        getijMaxArea(i,j+1)       
    return 0
            
n=int(input())
array=[]
for i in range(n):
    array.append(input())

ijMaxArea=[[0 for i in range(n)]for i in range(n)]
ijFlag=[[0 for i in range(n)]for i in range(n)]

maxArea=1
comArea=[]
for i in range(n):
        for j in range(n):
           if ijFlag[i][j]!='r':
               
               getijMaxArea(i,j)              
               temp=len(comArea)
               for k in comArea:
                   ijMaxArea[k[0]][k[1]]=temp
               maxArea=max(maxArea,ijMaxArea[i][j])
               comArea=[]

print (maxArea)
