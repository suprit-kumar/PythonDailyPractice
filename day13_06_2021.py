'''Python Program for Program to find area of a circle'''


def circle_area(radius):
    if isinstance(radius, int) or isinstance(radius, float):
        pi = 3.141
        area = pi * (radius ** 2)
        return "The area of the circle is: " + str(area) +" sq.m"

    else:
        return "Input must be int or float type"

call = circle_area(5)
print(call)


'''Python program to print all Prime numbers in an Interval'''