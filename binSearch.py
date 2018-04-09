def binSearch(array,num):

    if num not in array:
        return 0

    low,high=0,len(array)-1
    while low<=high:
        tmpkey = low+(high-low)//2
        if array[tmpkey]==num:
            return array[tmpkey]
        if array[tmpkey]>num:
            high = tmpkey-1
        if array[tmpkey]<num:
            low = tmpkey+1
    #print(tmpkey)
    return low

array=[1,2,3,4,5,6,7,8,9]
res=binSearch(array,9)
print(res)
