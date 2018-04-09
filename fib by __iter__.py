class Fib(object):

    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            temp = self.b
            self.n,self.a,self.b = self.n+1,self.b,self.a+self.b
            return temp
        raise StopIteration()
    
        
