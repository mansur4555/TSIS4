def evengen(n):
    return (num for num in range(n + 1) if num % 2 == 0)

n = int(input("Enter a number: "))
result = ', '.join(map(str, evengen(n)))
print(result)