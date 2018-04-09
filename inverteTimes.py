def getCalTimes(number):
    
    if number>2000000000:
        return False
    
    calTimes=0
    while number>=10:
        product=1
        while number:
            product=product*(number%10)
            number=number//10

        number=product
        calTimes=calTimes+1

    return calTimes
        
number=int(input())
print(getCalTimes(number))
        
