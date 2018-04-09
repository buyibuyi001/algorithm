'''
链接：https://www.nowcoder.com/questionTerminal/0c5d9dcb75c84551be2e162c01bc4c6a
牛牛手里有N根木棒,分别编号为1~N,现在他从N根里想取出三根木棒，使得三根木棒构成一个三角形,你能计算出牛牛有多少种取法吗?(考虑两种取法中使用的木棒编号有一个不一样就认为是不同的取法)。 
输入描述:
首先输入一个正整数N，接下来的一行共有N个正整数表示每个木棒的长度。
N ≤ 50, 木棒的长度 ≤ 10000.
输出描述:
输出一个整数表示方法数。
'''

def absDiff(a,b):
    return abs(a-b)
def getStickAssemblyKind(n,stick):
    if n>50:
        return False
    else:
        for i in stick:
            if i >10000:
                return False
            
    stickAssemblyKind=0
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if stick[i]+stick[j]>stick[k] and stick[i]+stick[k]>stick[j] and stick[j]+stick[k]>stick[i]:
                    if absDiff(stick[i],stick[j])<stick[k] and absDiff(stick[i],stick[k])<stick[j] and absDiff(stick[j],stick[k])<stick[i]:
                        stickAssemblyKind=stickAssemblyKind+1

    return stickAssemblyKind

n=int(input())
stick=list(map(int,input().split(' ')))
res=getStickAssemblyKind(n,stick)
print(res)
