import re
def text_match(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'YES'
        else:
                return 'NO'

print(text_match(input('Enter the stirng to match:')))
