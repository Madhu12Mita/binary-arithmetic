# decimal to binary

def decToBinary(num,list):
    if num>=1:
        decToBinary(num//2,list)
    list.append(num%2)
    
def add(l1,l2):
    pass

def sub(l1,l2):
    pass

def mul(l1,l2):
    pass

l1 = []
l2 = []

a = int(input("first num: "))
b = int(input("second num: "))

decToBinary(a,l1)
decToBinary(b,l2)

n = int(input("enter 1 for add, 2 for sub, 3 for mul"))

if(n==1):
    add(l1,l2)
elif(n==2):
    sub(l1,l2)
elif(n==3):
    mul(l1,l2)
else:
    print("enter proper input")
