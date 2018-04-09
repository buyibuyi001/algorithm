def reverseStr(astring):
    newstring=''
    for i in range(len(astring)):
        newstring += astring[-1-i]

    return newstring

astring="good"
res=reverseStr(astring)
print(res)
