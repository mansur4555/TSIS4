def divis(n):
    return (num for num in range(n + 1) if num % 3 == 0 and num % 4 == 0)

x = int(input())
result = divis(x)

for nu in result:
    print(nu)