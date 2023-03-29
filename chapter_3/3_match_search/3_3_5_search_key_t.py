import re

pattern = r'\bt=0.[0-9+]+\b'

try:
    res = re.search(pattern, input())
    print(res.group())
except AttributeError as ex:
    print(f'Error: ', ex)
