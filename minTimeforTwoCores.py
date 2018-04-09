def minTimeforTwoCores(n,nlist):
    
    nlist_sum=sum(nlist)
    bag=nlist_sum//(2*1024)
    bag_list=[0]*(bag+1)     
    
    for num in nlist:
        for j in range(bag,-1,-1):  #because j is sum of list,so j is always bigger than alist[i]                            
            if j>=num//1024:
                bag_list[j]=max(bag_list[j],bag_list[j-num//1024]+num)
        
    return (nlist_sum-bag_list[bag])

n=int(input())
nlist=list(map(int,input().split()))
res=minTimeforTwoCores(n,nlist)
print(res)
