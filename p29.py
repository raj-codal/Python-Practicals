import re
str = input('Enter the string to be validated:')
if re.match('^a',str):
    print('YES')
else:
    print('NO')
