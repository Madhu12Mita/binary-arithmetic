class arthimetic:
    def __init__(self,a,b):
        if a<0:
            l=self.complement(a)
        else:
            l=self.binary(a)
        if b<0:
            l1=self.complement(b)
        else:
            l1=self.binary(b)
    def complement(self,a):
        
a=int(input())
b=int(input())