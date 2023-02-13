'''
    BINARY ARTHMETIC
    ----------------
    AUTHORS: K MADHU MITA AND R JAHNAVI
    * This code conatins the arthimetic operations which are performed using binary numbers.
    * The binary numbers are taken in the form of list.
    * The arthimetic operations performed are
        1.Addition
        2.Subtarction
        3.Multiplication
        4.Division
        5.Power
        6.Modulus
        7.Factorial
'''
# decimal to binary
def decToBinary(num,list):
    # The given decimal number is converted to a binary string of length 32 and then it converted to binary list

    binary = '{:032b}'.format(num)
    for i in binary:
        i = int(i)
        list.append(i)

# binary to decimal
def binToDecimal(list):
    # A binary number is passed as a list and is converted to decimal number
    '''
        pseudo code
        1.START
        2. The given list is reversed. 
        3. Take a counter and result and initialize them to 0.
        4. Repeat step 4 and 5 for every element in list.
        5. Multiply the element is list with 2 raised to the power of counter.
        6. Add it to result.
        7. Return the value.
        8. END
    '''
    list.reverse()
    pow = 0
    val = 0
    for i in list:
        val = val + i*(2**pow)
        pow += 1
    return val

# 2's complement
def twos_complement(list):
    # The binary number is passed as a list and computes the 2s complement
    '''
        pseudo code
        1. START
        2. Repeat step 3 for each element in list.
        3. If the element is 0 make it 1 and viice-versa.
        4. Add 1 to the existing list.
        5. Return the list.
        6. END
    '''
    for i in range(len(list)):
        if list[i]==1: list[i]=0
        else: list[i]=1
    one = []
    decToBinary(1,one)
    return(addition(list,one))

# addition function  
def addition(l1,l2):
    #  2 binary numbers are passed as parameters to perform bunary addition
    '''
        pseudo code
        INPUT- list1, list2
        1. START
        2. Reverse the lists (This is done as we start addition from LSB)
        3. Intialize carry as zero
        4. For each element in list1, repeat step 5 and 6.
        5. Add the element in list1 with corresponding element in list2 and store it in a variable val.
        6. Check for carry-
            6.1 If val is 2, then make val 0 and carry 1
            6.2 If val is 3, then make val 1 and carry 1
            6.3 else make carry 0
        7. Reverse result 
        8. Return result.
        9.END
    '''
    result = []
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
        else:
            carry = 0
        result.append(val)
    result = result[::-1]
    return result

# subtraction function
def subtraction(l1,l2):
    # 2 binary numbers are given input to perform binary subtraction
    """
        pseudo code
        1. START
        2. Compute 2s complement of second number by calling 2s complement method.
        3. Add the 2s complement of second number to first number.
        4. Return the result.
        5. END
    """
    l2=twos_complement(l2)
    result=addition(l1,l2)
    return result

# multiplication function
def multiplication(l1,l2):
    # 2 binary numbers are given as input to perform multiplication
    '''
        pseudo code
        INPUT- list1, list2
        1. START
        2. Reverse the given binary lists.
        3. Intialize a counter i as 0.
        4. Intialize a list of 0s for storing final result.
        5. For each element in list2, repeat step 6-11.
        6. Intialize an empty  list (for keeping the result of multiplication in each iteration) current_product.
        7. Append i number of 0s to current_product.
        8. For every element in list1 multiply with current element in list2 and append it to current_product.
        9. Reverse current_product.
        10. Add current_product to result
        11. Incerement counter i by 1
        12. return result.
    '''
    l1=l1[::-1]
    l2=l2[::-1]
    result=[0]*32
    i=0
    for digY in l2:
        current_product=[]
        for j in range(i):
            current_product.append(0)
        for digX in l1:
            current_product.append(digX*digY)
        current_product.reverse()
        result=addition(result,current_product)
        i+=1
    return result

# division function
def division(l1,l2):
    # 2 binary numbers are given as input to perform division
    '''
        pseudo code
        START
        1. Intialize a list of 0s for quotient.
        2. Intialize dividend as list1 and divisor as list2.
        4. Convert dividend and divisor to decimal.
        3. Repeat step 4 and 5 until divididen is greater than or equal to divisor.
        4. Subtract dividend from divisor .
        5. Add one to quotient.
        6. The dividend remaining after the loop is remainder
        7. Return quotient and remainder.
        END
    '''
    zero_list = []
    decToBinary(0,zero_list)
    quotient = zero_list
    dividend = binToDecimal(l1)
    divisor = binToDecimal(l2)
    while dividend >= divisor:
        dividend -= divisor
        one_list = []
        decToBinary(1,one_list)
        quotient = addition(quotient,one_list)
    return quotient,dividend

def power(l1,l2):
    # 2 binary numbers are given as input to perform power
    '''
        pseudo code
        1.START
        2. Intialize a list for result as 1.
        3. Convert the list2 to decimal and store it in counter variable.
        4. Repeat step 5 and 6 until counter becomes less than 0.
        5. Multiply list1 and result and store it in result.
        6. Decrement counter by 1.
        7. Return result.
        8. END
    '''
    result=[]
    decToBinary(1,result)
    counter=binToDecimal(l2)
    while counter>0:
        result=multiplication(l1,result)
        counter-=1
    return result

# modulus function
def modulus(l1,l2):
    ## 2 binary numbers are given as input to perform modulus
    '''
        pseudo code
        1.START
        2. Perform division for the given two numbers.
        3. Return the remainder
    '''
    q,rem = division(l1, l2)
    return rem

# factorial function
def factorial(l1):
    ## 1 binary number is given as input to perform factorial
    '''
        pseudo code
        1.START
        2. Intialize one_list,result list with 1.
        3. Convert the given number to decimal and store it in i.
        4. Repeat steps 5-7  until i becomes 0.
        5. Multiply list1 and result and store it in result.
        6. Subtract one_list from list1 and store it in list1.
        7. Decrement i by 1.
        8. Return result.
        9. END

    result1 = []
    decToBinary(1,result1)
    one_list = []
    decToBinary(1,one_list)
    i = binToDecimal(l1)

    while(i > 0):
        result1 = multiplication(l1,result1)
        l1 = subtraction(l1,one_list)
        print("sub")
        #print(l1)
        i -= 1
    return result1
'''

# Driver code
# Lists are intialized to store the binary stream of given numbers
list1 = []
list2 = []

# input of 2 decimal numbers
while(1):
    first_num = int(input("first num: "))
    second_num = int(input("second num: "))
    # condition to check the overflow condition ie the result should not exceed 2^32 and the program accepts integers
    if first_num * second_num >= 4294967295:
        print("Overload Case, enter again...")
    else:
        break

# converting decimal to list of 32 bit binary numbers
decToBinary(first_num,list1)
decToBinary(second_num,list2)

# Menu driven code to select the arthimetic operation
while(1):
    n = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power, 6 for modulus, 7 for factorial:  "))
    if(n==1):
        # calling the addition function to compute binary addition
        result = addition(list1,list2)
        print(result)
        # converting the binary result to integer
        print(binToDecimal(result))
        break
    elif(n==2):
        # condtion to check if the first number is smaller than the second number
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
        # Multiplication
        result=multiplication(list1,list2)
        print(result)
        print(binToDecimal(result))
        break
    elif(n==4):
        # Division
        if second_num==0:
            print("Cannot perform division")
            break
        result,remainder=division(list1,list2)
        print("quotient: ", result)
        print(binToDecimal(result))
        print("remainder: ", remainder)
        break
    elif(n==5):
        # Power
        result=power(list1,list2)
        print(result)
        print(binToDecimal(result))
        break
    elif(n==6):
        # Modulus
        result=modulus(list1,list2)
        print(result)
        break
    elif(n==7):
        # factorial
        result1= factorial(list1)
        print("factorial of " , first_num , " : ", result1)
        print(binToDecimal(result1))
        result2= factorial(list2)
        print("factorial of " , second_num , " : ", result2)
        print(binToDecimal(result2))
        print("hello")
        break
    else:
        # incorrect input
        print("Enter proper input")
