'''class ListNode(object):
    def __init__(self):
        self.val=val
        self.next=None'''
from functools import reduce
def mergeTwoLists(listA,listB):

    if listA==[] or listB==[]:
        return listA or listB
    
    i,j,resList,iLen,jLen=0,0,[],len(listA),len(listB)
    while i<iLen and j<jLen:
        if listA[i]<listB[j]:
            resList.append(listA[i])
            i+=1
        else:
            resList.append(listB[j])
            j+=1
    
    if i==iLen:resList[-1:]=listB[j:]            
    if j==jLen:resList[-1:]=listA[i:]


    return resList

listA=[1,3,5,7,9]
listB=[2,4,6,7,9]
listC=[10,11,24,56]
listD=[25,78,100,109]
print(mergeTwoLists(listA,listB))
print(reduce(mergeTwoLists,[listA,listB,listC,listD]))
                              
            
        
    
    

    
