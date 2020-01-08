def factorial(x):
    f = 1
    while(x >= 1):
        f *= x
        x -= 1
    return f
i = int(input("Enter a number:"))
print(factorial(i))
