

nums=[[1,2,3,4],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

def bfs(nums):
   
    if nums==[]:
        return

    stack=[nums]
    nums_len=len(nums)

    while stack:
        print(stack.pop(0))
        for i in range(nums_len):
            if nums[i]!=[] and nums[i][0]:
                stack.append(nums[i].pop(0))
                print(stack)            

    return 0
bfs(nums)
