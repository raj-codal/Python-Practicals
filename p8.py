# *
# **
# ***

n = int(input("enter n:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

# 1
# 12
# 123

n = int(input("enter n:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end="")
    print()

#   * 
#  * * 
# * * * 

n = int(input("enter n:"))
for i in range(0,n):
    for j in range(0 , n - i):
        print(" ",end="")
    for j in range(0, i + 1): 
        print("* ",end="")
    print()

#   1
#  22
# 333

n = int(input("enter n:"))
for i in range(0,n):
    for j in range(0 , n - i):
        print(" ",end="")
    for j in range(0, i + 1): 
        print(i+1,end="")
    print()
