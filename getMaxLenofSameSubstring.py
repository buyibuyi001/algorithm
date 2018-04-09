'''
链
牛牛有两个字符串（可能包含空格）,牛牛想找出其中最长的公共连续子串,希望你能帮助他,并输出其长度。
输入描述:
输入为两行字符串（可能包含空格），长度均小于等于50.
输出描述:

输出为一个整数，表示最长公共连续子串的长度。
'''
def maxSameSubarray(str1,str2):

    len1,len2=len(str1),len(str2)
    res=0

    for i in range(len1):
            for j in range(len2):
                itmp,jtmp,tmpMaxLen=i,j,0
                while itmp<len1 and jtmp<len2  \
                      and str2[jtmp]==str1[itmp]:
                    tmpMaxLen+=1
                    itmp,jtmp=itmp+1,jtmp+1
                res=max(res,tmpMaxLen)
    return res

str1=input()
str2=input()
res=maxSameSubarray(str1,str2)
print(res)
