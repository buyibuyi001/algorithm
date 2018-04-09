def fib(max):
    n,a,b=0,0,1
    L=[]
    while n<max:
        L.append(b)
        n,a,b=n+1,b,a+b
    return L

print (fib(8))
