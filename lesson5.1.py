import string
import keyword

name = str(input('Enter variable name: '))
allowed = string.ascii_lowercase + string.digits + '_'

if name[0].isdigit():
    print('False')
elif not all(c in allowed for c in name):
    print('False')
elif name in keyword.kwlist:
    print('False')
else:
    print('True')