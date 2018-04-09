#  30%   pass

from functools import reduce

def visit(cur_time_sum,n):
    if n==time_list_len:
        return 0
    max_time_set.add(max(cur_time_sum,time_list_sum-cur_time_sum))
    #print(cur_time_sum,n,max_time_set)

    visit(cur_time_sum,n+1)
    visit(cur_time_sum+time_list[n],n+1)
    
n=int(input())
time_list=list(map(int,input().split()))

time_list_len=len(time_list)
time_list_sum=sum(time_list)
max_time_set=set()
min_time=time_list_sum

visit(0,0)

print(reduce(min,max_time_set))
