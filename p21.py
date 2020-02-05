from itertools import groupby
def elementCounter(inputList):
    l1 = sorted(inputList)
    groupItr = groupby(l1)
    output = {}
    for key, group in groupItr:
        output[key] = sum(1 for x in group)
    return output

inputList = [i for i in input("Enter list:").strip().split()]
print(elementCounter(inputList))
