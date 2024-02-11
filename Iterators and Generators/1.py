N = int(input())
generator1 = (x ** 2 for x in range(N))

for i in range(N):
    print(next(generator1))