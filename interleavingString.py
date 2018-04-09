
def isInterleave(s1, s2, s3):
    # write your code here
        
    s1len,s2len=len(s1),len(s2)
    if s1len==0 or s2len==0:
        return s1==s3 or s2==s3
    ijtemp=[[0 for j in range(s2len+1)] for i in range(s1len+1)]
    ijtemp[0][0]=True
        
    for i in range(1,s1len+1):
        ijtemp[i][0]=ijtemp[i-1][0] and s1[i-1]==s3[i-1]
        
    for j in range(1,s2len+1):
        ijtemp[0][j]=ijtemp[0][j-1] and s2[j-1]==s3[j-1]
    
    for i in range(1,s1len+1):
        for j in range(1,s2len+1):  
            ijtemp[i][j]=ijtemp[i-1][j] and s1[i-1]==s3[i+j-1] or \
                         ijtemp[i][j-1] and s2[j-1]==s3[i+j-1]
                      
    return ijtemp[s1len][s2len]

s1 = "aabcc"
                                    
s2 = "dbbca"

s3 = "aadbbbaccc"
            
print(isInterleave(s1,s2,s3))
        
