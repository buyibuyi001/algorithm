
import copy
def permute(nums):     
        numslen=len(nums)
        book=[ 0 for i in range(numslen) ]
        
        visit(nums,0,book,[],numslen)
        
        return res
        
def visit(nums,dpt,book,array,numslen):
            
            if  dpt==numslen and array not in res:
                res.append(array)
                return             
            
            for i in range(numslen):
                
                if  book[i]==0:
                    mybook=copy.deepcopy(book)
                    mybook[i]=1
                    
                    visit(nums,dpt+1,mybook,array+[nums[i]],numslen)
res=[]
nums=[1,2,3]
print(permute(nums))

#use add to destroy copy
