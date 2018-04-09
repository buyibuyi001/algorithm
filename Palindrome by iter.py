def GetRes(string):
    index, strlen, find= 0, len(string) , 0
    res =strlen
    
    while index < strlen-1:
        i, j= index, 0,         
        while i< index+ (strlen-index)//2:     
            if string[i] != string[strlen-1-j]:
                break;             
            if i== index+(strlen-index)//2-1:
                find= 1               
            i,j= i+1, j+1    
        if find==1: break         
        else:       index +=1  
        
    return res +index    # for the first time index is add once more, to minus code lines

string="abcba"
res=GetRes(string)
print(res)
