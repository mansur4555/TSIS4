import math
def area(num, lside):
    apo = lside / (2 * math.tanh(180/num))
    return (apo * (num * lside)) / 2


n = input("Input number of sides: ")
n = int(n)
s = input("Input the length of a side: ")
s = float(s)
print("The area of the polygon is:", area(n, s))