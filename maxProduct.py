
def maxProduct(nums):

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

     return res
         

nums=[2,3,-2,4]   
print(maxProduct(nums))
            
        

    
