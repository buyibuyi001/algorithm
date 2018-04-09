

def delDup(s1):
    s1len=len(s1)
    s3=s1[0]
    s3len=1
    for i in range(1,s1len):
        for j in range(s3len):       
            if s1[j]==s1[i]:
                break
            if j==s3len-1:
                s3+=s1[i]
                s3len+=1
                
    return s3

s1=input()
res=delDup(s1)
print(res)      

#本例子内层循环变化右界，一般内层循环变化左界。
