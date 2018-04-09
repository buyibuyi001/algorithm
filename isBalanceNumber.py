def isBalanceNum(a):

    if len(a)==1:
        return 'NO'
    for i in range(len(a)):
        product1=1
        product2=1
        for j in range(0,i+1):
            product1=product1*int(a[j])
        for j in range(i+1,len(a)):
            product2=product2*int(a[j])
        print (product1,product2)
      
    if product1==product2:
        return 'YES'
    else:
        return 'NO'

a=input() 
print(isBalanceNum(a))
