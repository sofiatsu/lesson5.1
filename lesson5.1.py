import string
import keyword

name = str(input('Enter variable name: '))
allowed = string.ascii_lowercase + string.digits + '_'

if name not in allowed:
    print('False')
elif name[0].isdigit():
    print('False')
elif name in keyword.kwlist:
    print('False')
elif name.count('_') > 1:
    print('False')
elif name.isupper():
    print('False')
else:
    print('True')