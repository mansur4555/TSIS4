def numb(n):
    return (num for num in range(n, -1, -1))

x = int(input())
result = numb(x)

for it in result:
    print(it)