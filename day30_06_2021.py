'''Python Program for Program to find area of a circle'''


def find_circle_area():
    pi = 3.141
    radius = float(input("Enter radius of the circle\n"))
    print("The area of the circle is: ", pi * (radius * radius))


# find_circle_area()


'''Python program to print all Prime numbers in an Interval'''


def print_prime_numbers(n):
    '''
    Decrease number count one everytime in loop
    In for loop start from 2 to the last number to check n is divisible by other number or not
    If divisible then break else appned in list
    '''
    prime_number = []
    if n > 1:
        while n >= 1:
            for i in range(2,n):
                if n % i == 0:
                    break
            else:
                prime_number.append(n)
            n = n - 1
    print('prime numbers ->', prime_number)


# print_prime_numbers(23)


'''Python program to check whether a number is Prime or not'''

def check_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('not prime')
                break
        else:
            print('prime number')
    else:
        print('not prime')

check_prime(23)