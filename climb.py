import time

def decorator(func):
    #print("start ",time.time())
    def wrapper(*args,**kwargs):       
        func(*args,**kwargs)   
    return wrapper

@decorator
def climb(n,steps):    
    count=0
    if n==0:
        count=1
    if n>0:
        for step in range(1,steps+1):
            count += climb(n-step,steps)
    return count

#start=time.time()
#print("start  climb",start)
print( climb(20,2))
print("end", time.time())
#print("end    climb",time.time()-start)

#@decorator
def climb2(n,step):
    res=[0 for i in range(n+1)]
    for i in range(n+1):
        for j in range(1,step+1):
            if i==0: res[i+j]=1
            if i+j<n+1:                
                res[i+j] += res[i]
    return res[n]


start=time.time()
print("start  climb2",start)
print( climb2(40,2))
print("end    climb2",time.time()-start)

