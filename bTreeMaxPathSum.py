from sys import maxsize
finmax=-maxsize

class Solution:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self,root):
        getMaxPathSum(root)
        return finmax

    def getMaxPathSum(self,root):
        if root==None: return 0
        lleft=getMaxPathSum(root.left)
        lright=getMaxPathSum(root.right)

        curSum=max(max(lleft+root.val,lright+root.val),root.val)
        curMax=max(curSum,lleft+lright+root.val)
        finmax=max(finmax,curMax)

        return curSum
