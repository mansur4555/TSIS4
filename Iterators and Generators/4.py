def Squares(a, b):
    return (num * num for num in range(a, b + 1))
a = int(input())
b = int(input())
result = Squares(a, b)

for it in result:
    print(it)