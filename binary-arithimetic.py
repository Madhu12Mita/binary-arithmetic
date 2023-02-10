# decimal to binary

def decToBinary(num,list):
    if num>=1:
        decToBinary(num//2,list)
    list.append(num%2)
    return list
    
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
