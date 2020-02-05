l1 = [i for i in input("enter the elements of the list1:").strip().split()]
l2 = [i for i in input("enter the elements of the list2:").strip().split()]
d = dict()
for i,j in zip(l1,l2):
    d[i] = j
print(d)
