
def maxProduct(nums):

    nums_len=len(nums)
    res=nums[0]

    if nums_len==1:
        return res

    for j in range(nums_len):
        product= temp_max=nums[j]
        
        for i in range(j+1,nums_len):
            product=product*nums[i]
            temp_max=max(temp_max,product)

            print(temp_max,product)
            
        res=max(res,temp_max)

    return res
nums=[2,3,-2,4]
print(maxProduct(nums))
