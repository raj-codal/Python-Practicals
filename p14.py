def fibonacci(n):
    l = []
    if n == 1: l = [1]
    elif n > 1: l = [1,1]
    if n > 2:
        for i in range(2,n):
            l += [(l[-1]+l[-2])]
    print(l)

n = int(input("Enter n:"))
fibonacci(n)
