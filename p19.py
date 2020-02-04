def words(string):
    return len(string.strip().split())
y = input("Enter string:")
print("# of words:",words(y))
