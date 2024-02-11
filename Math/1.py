import math
x = input()
x = int(x)
print(math.radians(x))

#OR

def rad(y):
    x = math.pi * y / 180 
    return x
#instead of math.pi you can print 3.14(but it is not exactly number)
num = float(input())
print(rad(num))