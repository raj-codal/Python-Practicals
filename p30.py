import re
def text_match(text):
    patterns = '\w+\S*$'
    return re.search(patterns,  text).group()
                

print(text_match(input('Enter the stirng to match:')))
