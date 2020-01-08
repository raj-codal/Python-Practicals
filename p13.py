def isPrime(x):
    for i in range(2,int(x ** 0.5)+1):
        if x % i == 0: return False
    return True
x = int(input("Enter N:"))
print("isPrime:",isPrime(x))
