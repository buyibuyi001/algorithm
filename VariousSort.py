# 非线性时间比较类型排序有：
#   交换排序：比较交换排序,冒泡排序,快速排序
#   插入排序：简单插入排序,希尔排序
#   选择排序：简单选择排序,堆排序
#   归并排序：两路归并排序,多路归并排序

# 线性时间比较类排序
#   计数排序
#   桶排序
#   基数排序

# python 递归堆栈占时间，速度太慢,递归要小心，容易溢出
def timing(func):
    '''适用于非递归函数'''
    def decorator(*args):  #args 直接包含原参数
        #print (args)
        t=time()
        res=func(*args)
        print(func.__doc__,' ',time()-t,type(res) )
        if isinstance(res,list):
            return res   #对函数，函数返回值res就是结果
        if isinstance(res,func):
            return res.value() #实例，因为实例没有返回值，其返回值被存储在result中，所以由此返回   
    return decorator

@timing
def compareSort(L ):
    '''比较排序算法'''
    nl=len(L)
    for i in range(nl-1):
        for j in range(i+1,nl):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L
@timing
def chooseSort(L):
    '''选择排序算法'''
    nl=len(L)
    for i in range(nl-1):
        index=i
        for j in range(i+1,nl):
            if L[index]>L[j]:
                index=j
        if index !=i:
            L[i],L[index]= L[index],L[i]
    return L
@timing
def bubbleSort(L):
    '''冒泡排序算法'''
    nl=len(L)
    #print( L)
    for i in range(nl-1):
        for j in range(nl-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]= L[j+1],L[j]
    return L
@timing
def bubbleSort1(L):
    '''冒泡排序算法1'''
    nl=len(L)
    #print( L)
    for i in range(nl-1):
        flag=0
        for j in range(nl-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]= L[j+1],L[j]
                flag=1
        if flag==0:break
    return L

@timing
def bubbleSort2(L):
    '''冒泡排序算法2'''
    nl=len(L)
    lastswapindex=nl-1
    for i in range(nl-1):
        hasorder= True        
        for j in range(lastswapindex):
            if L[j]>L[j+1]:
                L[j],L[j+1]= L[j+1],L[j]
                hasorder=False
                lastswapindex=j            
        if hasorder !=False :break
    return L

@timing
def insertSort(L):
    '''插入排序算法'''
    for i in range(1,len(L)):
        index=i-1
        curref=L[i]  #必须使用这个变量,因为后边L[i]被覆盖了
        while index>=0  and L[index]>curref:
            L[index+1]=L[index]
            index -=1
        L[index+1]=curref
    return L

        
@timing
def quickSortShell(L):  #对递归方法的调用
    '''快速排序算法'''

    def quickSort(L):
        if L==[]: return L
        ref=L[0]
        l= [x for x in L[1:] if x<ref ] 
        r= [x for x in L[1:] if x>=ref]
        return quickSort(l) + [ref]+ quickSort(r)
    return quickSort(L)

@timing
def quickSortShell1(L):  #对递归方法的调用
    '''快速排序算法1'''   
    def quickSort1(L):  # 比第一个提升了性能
        if L==[]: return L  
        ref=L[0]
        ll= quickSort1( [x for x in L[1:] if x<ref ] )
        rl= quickSort1( [x for x in L[1:] if x>=ref] )
        return ll + [ref]+ rl
    return quickSort1(L)

@timing
def quickSortShell2(L):  #对递归方法的调用
    '''快速排序算法2'''    
    def quickSort2(L):
        if L==[]: return L
        ref=L[0]
        l,r=[],[]
        for x in L[1:]:
            if x<ref: l.append(x)
            else:     r.append(x)
        return quickSort2(l) + [ref]+ quickSort2(r)
    return quickSort2(L)

@timing
def quickSortShell3(L):  #对递归方法的调用
    '''快速排序算法3'''
    
    def quickSort3(L, low, high):
        i = low 
        j = high
        if i >= j:
            return L
        key = L[i]
        while i < j:
            while i < j and L[j] >= key:
                j = j-1                                                             
            L[i] = L[j]
            while i < j and L[i] <= key:    
                i = i+1 
            L[j] = L[i]
        L[i] = key 
        quickSort3(L, low, i-1)
        quickSort3(L, j+1, high)
        return L
    return quickSort3(L,0,len(L)-1)
    
@timing
class MergeSort():
    #类内方法调用只能由init 吃进参数,__init__不能有None之外的返回值
    '''归并排序算法'''
    def __init__(self,L):
        self.L=L        
        self.res= self.mergesort(L,len(L))     
    def mergesort(self,L,nl):  # O means ordered, self上带有属性值，所有可以调用self.attrs
        if nl==1: return L  #这里为0 就无限递归了
        #print ( ) 
        mid=nl//2
        LA, RA = L[:mid], L[mid:]
        OL = self.mergesort(LA,len(LA))
        OR = self.mergesort(RA,len(RA))   
        return self.merge(OL,OR)     
    def merge(self,orderL,orderR):
        res=[]
        while len(orderL)>0 and len(orderR)>0:
            res.append( orderL.pop(0) if orderL[0] < orderR[0]  else orderR.pop(0) )
        res += orderL+orderR
        return res
    def value(self):
        return self.res
   
@timing
class HeapSort():
    '''错的堆排序算法class'''
    def __init__(self,L):
        self.res=self.__heapsort(L)       
                     
    def __heapsort(self,L):
        nl=len(L)
        for i in range(nl-1,-1,-1):    #外层循环用来交换堆顶最大数      
            for j in range( nl//2,-1,-1):  #内层循环从倒数第二层开始一层层地将最底层或中间层的大数捞到堆顶
                ceil=j
                left = 2*j+1
                right= 2*j+2            
                if left<i+1 and L[left]> L[ceil]:
                    ceil = left
                if right<i+1 and L[right]>L[ceil]:
                    ceil = right
                if ceil!=j:
                    L[ceil],L[j]=L[j],L[ceil]
            L[0],L[i] = L[i],L[0]
        return L

    def value(self):
        return self.res

            
@timing
class HeapSort1():  # 错的堆排序
    '''错的堆排序1class'''
    def __init__(self,L):
        self.res=self.__heapsort(L)       
                     
    def __heapsort(self,L):
        nl=len(L)
        for i in range(nl-1,-1,-1):    #这层循环用来交换堆顶最大数      
            for j in range( nl//2,-1,-1):  #从倒数第二层开始将最底层的大数捞上来
                ceil=j
                left = 2*j+1
                right= 2*j+2            
                if left<i+1 and L[left]> L[ceil]:
                    ceil = left
                if right<i+1 and L[right]>L[ceil]:
                    ceil = right
                if ceil!=j:
                    L[ceil],L[j]=L[j],L[ceil]
            L[0],L[i] = L[i],L[0]
        return L

    def value(self):
        return self.res

@timing
def heapsort(L):
    '''堆排序算法 '''
    # 构造最大堆，从倒数第二层层层往上捞最大值，heapify中还会自己向下判定并转移数据

    def heapify(i, sufi):   # 向下判定并转移数据
        left=  2*i +1
        right= 2*i +2
        maxi =i
        if left<sufi and L[left]>L[maxi]:
            maxi=left
        if right<sufi and L[right]>L[maxi]:
            maxi=right
        if (maxi!=i):
            L[i],L[maxi] = L[maxi],L[i]
            heapify(maxi,sufi )

    nl =len(L)
    #buildheap
    for i in range(nl//2,-1,-1):
        heapify(i,nl)
    #print( 'maxheap', L)
    for i in range(nl-1,-1,-1):  #交换队尾数据
        L[0],L[i]= L[i],L[0]
        heapify(0, i)
    return L

@timing
def heapsort1(L):
    '''堆排序算法1 '''  # from 网上阿里程序员，实测运行时间长
    

    def heapify(root_index, end_index):   # 向下判定
        max_child_index = root_index*2-1
        if max_child_index +1 <end_index:
            if L[max_child_index+1] > L[max_child_index]:
                max_child_index +=1           
        if L[max_child_index]>L[root_index-1]:
            L[max_child_index],L[root_index-1]=L[root_index-1],L[max_child_index]

    for end_index in range( len(L),1,-1):
        max_root_index = end_index//2
        for root_index in range(max_root_index,0,-1):
            heapify(root_index,end_index)
        L[0],L[end_index-1] = L[end_index-1],L[0]
    return L

@timing
def heapsort2(L):
    '''堆排序算法2 '''   #实测这个写法性能差，只在第一次构造最大堆，之后局部更新才快
    # 构造最大堆，从倒数第二层层层往上捞最大值，heapify中还会自己向下判定并转移数据

    def heapify(i, sufi):   # 向下判定并转移数据
        left=  2*i +1
        right= 2*i +2
        maxi =i
        if left<sufi and L[left]>L[maxi]:
            maxi=left
        if right<sufi and L[right]>L[maxi]:
            maxi=right
        if (maxi!=i):
            L[i],L[maxi] = L[maxi],L[i]
            heapify(maxi,sufi )

    nl =len(L)
    for i in range(nl-1,-1,-1):  #交换队尾数据     
        for j in range(nl//2,-1,-1): #buildheap
            heapify(j,i+1)    
        L[0],L[i]= L[i],L[0]
    return L

@timing
def countSort(L):
    '''计数排序算法'''
    nl=len(L)
    if nl<=1 : return L    
    imin, imax= min(L), max(L)     
    C=[0 for i in range( imax-imin+1) ]
    for num in L:
        C[num-imin]+=1
    j=0   
    for i in range(len(C)):   
        while C[i]>0:
            L[j]=i+imin
            j+=1
            C[i]-=1           
    return L

@timing
def bucketsort(L):
    '''桶排序算法'''
    szl=len(L)
    if szl==0: return L
    nmin, nmax =min(L), max(L)
    ctbucket= 5
    szbucket= (nmax-nmin)//ctbucket +1
    buckets=[[] for i in range(ctbucket)]
    for i in range(szl):
        buckets[ (L[i]-nmin)//szbucket].append(L[i])
    k=0
    for l in buckets:
        x=sorted(l)
        for j in range(len(x) ):
            L[k]=x[j]
            k+=1
    return L
             
@timing
def radixsort(L):
    '''基数排序算法 '''
    mod
    
    

if __name__ == "__main__":     #__name__ 是当前模块名,当模块被直接运行时模块名为 __main__
    #当模块直接运行时，以下代码块将运行; 当模块是被导入时，代码块不被运行
    from random import randint
    from time import time

    L=[]
    for i in range(100):
        L.append(randint(1,100))
    L=L*200;
    #print(len(L)  );   #print (L,'数据' )
    LL=compareSort(L[:]);      #print (LL);  #0.005
    print (LL==chooseSort (L[:]) );          #print (LL);  #0.005
    print (LL==bubbleSort (L[:]) );          #print (LL);  #0.31
    print (LL==bubbleSort1(L[:]));          #0.31
    print (LL==bubbleSort2(L[:]) );          #0.31
    print (LL==insertSort (L[:]) );          #0.31  
    print (LL==quickSortShell(L[:]));
    print (LL==quickSortShell1(L[:]));
    print (LL==quickSortShell2(L[:]));
    print (LL==quickSortShell3(L[:]));
    print (LL==MergeSort(L[:]) )  
    print (LL==HeapSort(L[:]) ) 
    print (LL==heapsort(L[:]) ) 
    print (LL==heapsort1(L[:]) ) 
    print (LL==heapsort2(L[:]) )
    print (LL==countSort(L[:]) )  #最好在函数内部使L=L[:]
    print (LL==bucketsort(L[:]) )



