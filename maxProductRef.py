def maxProduct( nums):
        # write your code here

        nums_len = len(nums)
        pos_product     =neg_product=nums[0]
        pos_product_tmp = neg_product_tmp=nums[0]
        res=nums[0]

        for i in range(1,nums_len):
            pos_product=max(nums[i], max(pos_product_tmp*nums[i],neg_product_tmp*nums[i]))
            neg_product=min(nums[i], min(pos_product_tmp*nums[i],neg_product_tmp*nums[i]))
            pos_product_tmp= pos_product
            neg_product_tmp= neg_product
            res=max(res,pos_product)
            print(nums[i],pos_product,neg_product)

        return res

        #一个的子序列，二个的子序列，多个的子序列，动态规划结合多个比较，能解决相当大的问题

nums=[6,0.5,2,3,-2,0.5]

print(maxProduct(nums))
            
