'''Python program to add two numbers'''


def print_sum():
    inp1 = int(input('Enter first number\n'))
    inp2 = int(input('Enter second number\n'))
    print("The sum of two number: ", inp1 + inp2)


# print_sum()

'''Maximum of two numbers in Python'''


def maximum_of_two_number():
    inp1 = int(input('Enter first number\n'))
    inp2 = int(input('Enter second number\n'))

    ans = inp1 if inp1 > inp2 else inp2
    print("The greater number is: ", ans)


# maximum_of_two_number()


'''Python Program for factorial of a number'''


def find_factorial():
    inp = int(input("Enter number to find factorial\n"))
    count = 1
    num = 1
    while count <= inp:
        num = num * count
        print(num ,"=",num,"*",count)
        count+=1

    print("Factorial of input " + str(inp) + " is:", num)
# find_factorial()

'''Python Program for simple interest'''

def find_simple_interest():
    principal_balance = float(input("Enter principal amount\n"))
    rate_of_interest = float(input("Enter interest rate %\n"))
    time_period = int(input("Enter time period in years\n"))

    final_amount = (principal_balance*rate_of_interest*time_period)/100
    print("Total amount after interest :",final_amount+principal_balance)

# find_simple_interest()

'''Python Program for compound interest'''

def find_compound_interest():
    principal_balance = float(input("Enter principal amount\n"))
    rate_of_interest = float(input("Enter interest rate %\n"))
    time_period = int(input("Enter time period in years\n"))

    amount = principal_balance * (pow((1+rate_of_interest/100),time_period))
    ci = amount - principal_balance

    print("The CI is :",ci)


# find_compound_interest()

'''Python Program to check Armstrong Number'''

def checkArmstrongNumber():
    num = int(input("Enter a number: \n"))
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        print(digit , '=',temp,'%',10)
        sum += digit ** 3
        print(sum, '+=', digit, '**', 3)
        temp //= 10
        print('temp //= 10',temp)
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


# checkArmstrongNumber()