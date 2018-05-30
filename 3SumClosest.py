



nums= [-1,2,1,-4]
target=1
nums_sum = sum(nums)

def closestSum(nums,target):


    nums_len= len(nums)
    if nums_len <=3:
        return sum(nums)
    res = sum(nums[:3])
    min_diff = res-target
    res_tuple= tuple (nums[0:3])


    for i in range(0,nums_len-2):
        for j in range(i+1,nums_len-1) :
            for k in range(j+1 ,nums_len):
                print (nums[:nums_len-2],nums[i+1:nums_len-1], nums[j+1:nums_len])
                tmp_sum = nums[i]+nums[j]+nums[k]
                diff= tmp_sum - target 
                if abs(diff)<abs(min_diff):
                    min_diff = diff
                    res = tmp_sum
                    res_tuple = (nums[i],nums[j],nums[k])

                if min_diff==0:
                    break
    return res,res_tuple

print (closestSum(nums,target))
