final_list = []
line = input("Enter the list of key value pairs (press enter twice for end):\n")
while (line != ""):
    final_list.append(tuple(line.split()))
    line = input()
print(sorted(tuple(final_list),key = lambda x:x[0])) # sorting based on 1st element of the tuple
