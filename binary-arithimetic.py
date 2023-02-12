# decimal to binary
def decToBinary(num,list):
    # if num>=1:

    #     decToBinary(num//2,list)

    # list.append(num%2)
    binary = '{:032b}'.format(num)
    for i in binary:
        i = int(i)
        list.append(i)

# binary to decimal
def binToDecimal(list):
    list.reverse()
    pow = 0
    val = 0
    for i in list:
        val = val + i*(2**pow)
        pow += 1
    return val

# 2's complement
def twos_complement(list):
    for i in range(len(list)):
        if list[i]==1: list[i]=0
        else: list[i]=1
    one = []
    decToBinary(1,one)
    return(addition(list,one))

# addition function  
def addition(list1,list2):
    result = []
    rev_l1 = list1[::-1]
    rev_l2 = list2[::-1]
    carry = 0
    for i,j in zip(rev_l1,rev_l2):
        val = i+j+carry
        if val==2:
            val = 0
            carry = 1
        elif val==3:
            val = 1
            carry = 1
        else:
            carry = 0
        result.append(val)
    result = result[::-1]
    return result

# subtraction function
def subtraction(list1,list2):
    list2=twos_complement(list2)
    result=addition(list1,list2)
    return result

# multiplication function
def multiplication(list1,list2):
    list1.reverse()
    list2.reverse()
    result=[0]*32
    i=0
    for digY in list2:
        current_product=[]
        for j in range(i):
            current_product.append(0)
        for digX in list1:
            current_product.append(digX*digY)
        current_product.reverse()
        result=addition(result,current_product)
        i+=1
    return result

def division(list1,list2):
    pass

def power(list1,list2):
    pass

def modulus(list1,list2):
    pass

# Driver code
list1 = []
list2 = []
# input of 2 decimal numbers
while(1):
    first_num = int(input("first num: "))
    second_num = int(input("second num: "))
    if first_num * second_num >= 4294967295:
        print("Overload Case, enter again...")
    else:
        break
# converting decimal to list of 32 bit binary numbers
decToBinary(first_num,list1)
decToBinary(second_num,list2)
# choosing operation to perform
while(1):
    n = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power, 6 for modulus:  "))
    if(n==1):
        result = addition(list1,list2)
        print(result)
        print(binToDecimal(result))
        break
    elif(n==2):
        if first_num<second_num:
            list1,list2=list2,list1
            result=subtraction(list1,list2)
            print(result)
            a=binToDecimal(result)
            a=a*-1
            print(a)
        else:
            result=subtraction(list1,list2)
            print(result)
            print(binToDecimal(result))
        break
    elif(n==3):
        result=multiplication(list1,list2)
        print(result)
        print(binToDecimal(result))
        break
    elif(n==4):
        result=division(list1,list2)
        break
    elif(n==5):
        result=power(list1,list2)
        break
    elif(n==6):
        result=modulus(list1,list2)
        break
    else:
        print("Enter proper input")