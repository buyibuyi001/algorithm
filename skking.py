def GetLen(i,j):

    if lenght[i][j] != 0:
        return lenght[i][j]
   
    ijmax=0
    ijnextlen=0
    for k in range(4):
        nx=i+ijnext[k][0]
        ny=j+ijnext[k][1]
        
        if 0<= nx <row and 0<= ny < col and height[i][j] >height[nx][ny]:
            ijnextlen=1+GetLen(nx,ny)
            ijmax=max(ijmax,ijnextlen)
            #print( nx,ny, ijmax, lenght[i][j])
    return ijmax

x=list( map( int,input().split(' ') ) )
row,col=x[0],x[1]
height= [ [] for i in range(row) ]
lenght= [ [0 for j in range(col)] for i in range(row) ]
#ijnext= [ [0,1],[0,-1],[-1,0],[1,0] ]
ijnext= [ [0,1],[1,0],[-1,0],[0,-1] ]
for i in range(col):
    height[i]= list(map(int,input().split(' ')))
    #print(height[i],'\n')    
#print(lenght,'\n')
     

maxlen=0
for i in range(row):
    for j in range(col):
        lenght[i][j]=GetLen(i,j)
        maxlen=max(maxlen, lenght[i][j])
        
print(maxlen) 
