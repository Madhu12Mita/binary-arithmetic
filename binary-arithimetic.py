# decimal to binary

def decToBinary(num,list):
    if num>=1:
        decToBinary(num//2,list)
    list.append(num%2)

def binToDecimal(list):
    list.reverse()
    pow = 0
    val = 0
    for i in list:
        val = val + i*(2**pow)
        pow += 1
    print(val)

    
def add(l1,l2):
    res = []
    rev_l1 = l1[::-1]
    rev_l2 = l2[::-1]
    carry = 0
    for i,j in zip(rev_l1,rev_l2):
        val = i+j+carry
        if val==2:
            val = 0
            carry = 1
        elif val==3:
            val = 1
            carry = 1

        res.append(val)
    res = res[::-1]
    print(res)
    binToDecimal(res)


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

n = int(input("enter 1 for add, 2 for sub, 3 for mul: "))

if(n==1):
    add(l1,l2)
elif(n==2):
    sub(l1,l2)
elif(n==3):
    mul(l1,l2)
else:
    print("enter proper input")
