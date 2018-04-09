def chooseKFromN(k,n,nlist,array,res):
    
    
    if not k:
        res.append(array)
        #print("after append",k,n,"nlist=",nlist,"array=",array,"res=",res)
        return res
    
    
    
    for i in range(len(nlist)-k+1):
        
        #print("before iter",k,n,i,"nlist=",nlist,"array=",array,"res=",res )
        chooseKFromN(k-1,n-1,nlist[i+1:],array+[nlist[i]],res)
    return res
        

nlist=[1,2,3,4,5,6]
k=4
n=6

res=chooseKFromN(k,n,nlist,[],[])

print(res)

#ter must think of what is changing to change the var
