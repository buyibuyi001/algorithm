def maxProdSubarray(nums):

    nums_len=len(nums)
    maxProd=minProd=nums[0]
    res=nums[0]

    for i in range(1,nums_len):       
        tmpMaxProd,tmpMinProd=maxProd,minProd
        maxProd=max(nums[i],max(tmpMaxProd*nums[i],tmpMinProd*nums[i]))
        minProd=min(nums[i],min(tmpMaxProd*nums[i],tmpMinProd*nums[i]))
        res=max(res,maxProd)
        print(maxProd,minProd,res)
    return res

nums=[1,0,-1,2,3,-5,-2]

print(maxProdSubarray(nums))
