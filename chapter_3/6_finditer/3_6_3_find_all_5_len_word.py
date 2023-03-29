import re

if res := re.finditer(r'\b\w{5}\b', input()):
    [print(r[0]) for r in res]