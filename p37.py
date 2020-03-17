import math
def E(ETF):
    e = 0
    for i in range(2, ETF):
        if math.gcd(i, ETF) == 1:
            e = i
            break
    return e

def D(ETF,e):
    i = 1
    while True:
        d = int((1 + i * ETF) / e)
        if d < ETF and d > 0 and (d * e) % ETF == 1:
            break
        i+=1
    return d


D1 = lambda a,b:a==1or-~b*D1(-b%a,a)/a

p = int(input("Enter p value : - "))
q = int(input("Enter q value : - "))
m = int(input(("Enter msg : - ")))
n = p * q
ETF = (p - 1) * (q - 1)
e = E(ETF)
d = D(ETF,e)
d1 = D1(ETF,e)
print(d,d1)
print("encryption is ")
c=(m**e)%n
print(c)
print("decryption is")
M=(c**d)%n
print(M)
