x,y,z = input("enter 3 number:").split()
x,y,z = int(x),int(y),int(z)
if x>=y and y>=z:
    print("max:",x)
elif y>=x and x>=z:
    print("max:",y)
else:
    print("max:",z)
