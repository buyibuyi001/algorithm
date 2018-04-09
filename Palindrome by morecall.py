
def IsTheStr(string,index,strlen):
       
    i,j= index, 0
    while i< index+(strlen-index)//2:
        if string[i] != string[strlen-1-j]:
            print( index,string[i],string[strlen-1-j])
            return 0
        else:
            i,j= i+1,j+1          
    
    return strlen+index

def GetRes(string):
    index,strlen=0,len(string)  
    res=IsTheStr(string,index,strlen)  
    while not res:
        index=index+1       
        res=IsTheStr(string,index,strlen)
    return res

string="abcde"
res=GetRes(string)
print(res)
