"""Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are """


def printFollowingFormat():
    print(
        "Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are")


# printFollowingFormat()


'''Write a Python program to get the Python version you are using'''
import sys

# print('Python version -->',sys.version)


'''Write a Python program to display the current date and time.'''
import datetime

now = datetime.datetime.now()
# print(now)
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

'''Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them'''


def printReverse():
    firstname = str(input('Enter Frist name\n'))
    lasttname = str(input('Enter last name\n'))

    concat_str = f'{firstname} {lasttname}'
    print(f'Name after reverse: {concat_str[::-1]}')


# printReverse()


'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.'''


def createListAndTuple():
    inp = str(input("Enter something with commma separte\n"))
    if ',' in inp:
        emp_list = list(inp.split(','))

        emp_tuple = tuple(emp_list)
        print(emp_list)
        print(emp_tuple)
    else:
        print('Wrong entry')


# createListAndTuple()


'''Write a Python program to accept a filename from the user and print the extension of that.'''


def printFileExtension():
    inp = str(input("Enter file name with extension\n"))
    if '.' in inp:
        check_dot_count = inp.count('.')
        if check_dot_count == 1:
            find_index = inp.index('.')
            print("File extension is: ", inp[find_index::])
        else:
            print("File name is having more than one dot")
    else:
        print("File doesn't have any extension")

        # Another Solution

        # extension = inp.split('.')
        # print(extension)
        # print("File extension is: ",extension[-1])


'''Takeway str.split() returns a list'''
# printFileExtension()


'''Write a Python program to display the first and last colors from the following list.'''


def firstAndLastColour():
    color_list = ["Red", "Green", "White", "Black", "yellow"]
    print('First colour: ', color_list[0])
    print('Last colour: ', color_list[-1])


firstAndLastColour()
