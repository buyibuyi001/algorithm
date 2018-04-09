#按照n&(n-1) 这种方法确实是比求余数快一些。

import time

def countOne(n):
    a=float(time.time())
    print(a)

    one_count=0
    while n!=0:
        if n%2==1:
            one_count+=1
        n=n//2
    b=float(time.time())
    print(b)
    print(b-a)
    return one_count

countOne(8)


def countOne1(n):
    a=float(time.time())
    print(a)

    one_count=0
    while n!=0:
        n=n&(n-1)
        one_count+=1
    b=float(time.time())
    print(b)
    print(b-a)
    return one_count

countOne1(8)
