# 10% AC
def getMinTimes(astring):

    strLen=len(astring)
    if strLen==1 or strLen==0:
        return 0    
    else:
        minTimes0,minTimes1=0,0
        i,j=1-1,strLen-1
        ref=astring[0]       
        tempStr=astring
        while i<j :
            while i<j and tempStr[i]==ref:
                i=i+1

            while i<j and tempStr[j]==tempStr[i]:
                j=j-1
            tempStr=tempStr[:i]+tempStr[j]+tempStr[i:j]+tempStr[i]+tempStr[j+1:]
            minTimes0=minTimes0+j-i+j-i-1          
            #print(i,j,tempStr,minTimes0)

        i,j,k=1-1,strLen-1,0   #BBGGB
        while astring[k]==ref:
            k=k+1
        if astring[k]!=ref:
            ref1=astring[k]
        tempStr=astring
        while i<j :
            while i<j and tempStr[i]==ref1:
                i=i+1

            while i<j and tempStr[j]==tempStr[i]:
                j=j-1     
            tempStr=tempStr[:i]+tempStr[j]+tempStr[i:j]+tempStr[i]+tempStr[j+1:]
            minTimes0=minTimes0+j-i+j-i-1 
            
            #print(i,j,tempStr,minTimes1)
        return min(minTimes0,minTimes1) 
        
astring=input()
print(getMinTimes(astring))
