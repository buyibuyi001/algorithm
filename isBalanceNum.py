
def isBalanceNum(nString):
    if len(nString)==1:
        return 'NO'
    for i in range(len(nString)):
        product1=1
        product2=1
        for j in range(0,i+1):
            product1=product1*int(nString[j])
        for j in range(i+1,len(nString)):
            product2=product2*int(nString[j])
        print(product1,product2)
      
    if product1==product2:
        return 'YES'
    else:
        return 'NO'

nString=input() 
print(isBalanceNum(nString))
