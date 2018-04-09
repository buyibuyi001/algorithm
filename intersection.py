

serlist=[]
def seriation(self,root):

    visit(root)
    return serlist

def visit(self,root):
    if root==None:
        return 0


def intersection( nums1, nums2):
        # write your code here
        nums3=set(nums1)-set(nums2)
        return set(set(nums1)-nums3)

nums1=[1,2,2,1]
nums2=[2,2]
print(intersection(nums1,nums2))
