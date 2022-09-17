'''Python Program for Program to find area of a circle'''


def circle_area(radius):
    if not isinstance(radius, (int, float)):
        return "Input must be int or float type"
    area = 3.141 * radius ** 2
    return f"The area of the circle is: {str(area)} sq.m"

call = circle_area(5)
print(call)


'''Python program to print all Prime numbers in an Interval'''