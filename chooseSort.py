def chseSort(nlist):

    nlist_len=len(nlist)
    for i in range(nlist_len-1):
        k=i
        for j in range(i+1,nlist_len):
            if nlist[k]>nlist[j]:
                k=j
        temp=nlist[i]
        nlist[i]=nlist[k]
        nlist[k]=temp
    return nlist
nlist=[1,4,2,7,9,3]
print(chseSort(nlist))

# use k to store the near bigger  number and then swap
