h = input("Height: " )
h = float(h)
a = input("Base 1: ")
a = float(a)
b = input("Base 2: ")
b = float(b)
def area(hei, bas1, bas2):
    return ((bas1 + bas2) / 2) * hei

print("Expected Output:", area(h, a, b))