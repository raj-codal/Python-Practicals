def greatest(x,y,z):
    if x>=y>=z or x>=z>=y:
        return x
    elif y>=x>=z or y>=z>=x:
        return y
    elif z>=x>=y or z>=y>=x:
        return z

x,y,z = input("enter 3 number:").split()
x,y,z = int(x),int(y),int(z)
print("max:",greatest(x,y,z))
