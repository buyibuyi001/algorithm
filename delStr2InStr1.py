def delS2InS1(s1,s2):
    
    s1len,s2len=len(s1),len(s2)
    i=0
    s3=''
    
    while i<s1len:
        if not s1EqualS2(i,i+1,s1len,s2len):
            s3+=s1[i]           
            i+=1           
        else:                        
            k=i
            i+=s2len
            while k-1>=0 and i<s1len and s1EqualS2(k-1,i,s1len,s2len):
                s3=s3[:-1]
                i+=s2len-1
                k-=1                
        #print(i,s3)             
    return s3

def s1EqualS2(i,j,s1len,s2len):
    #print('i==',i)
    if i<s1len and j<s1len and s1[i]==s2[0]:       
        for k in range(1,s2len): 
            if j+k-1>=s1len or s1[j+k-1]!=s2[k]:
                break;           
            return True   
    return False

s1='tomcat is a male ccatat'
s2='cat'
res=delS2InS1(s1,s2)
print(res)
   
#ccatat 这里对消，所以这里开循环，对应第二个while
#while 也能条件判断，但是它的作用更多，还能循环
    
