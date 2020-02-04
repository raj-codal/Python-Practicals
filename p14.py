def fibonacci(n):
    l = []
    if n >= 1: l = [1,1]
    if n >= 2:
        while l[-1] <= n:
            l += [(l[-1]+l[-2])]
        l.pop(-1)
    print(l)

n = int(input("Enter n:"))
fibonacci(n)
