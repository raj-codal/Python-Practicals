n = int(input("Enter number:"))
print("number:",("odd","even")[n%2==0])

#or

n = int(input("Enter number:"))
print("number:","even" if n % 2 == 0 else "odd")
