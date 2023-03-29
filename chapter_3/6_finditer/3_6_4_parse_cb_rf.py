import re

if res := re.finditer(r'(?<=>)[\d]+,[\d]+ ₽(?=<)', input()):
    [print(r[0]) for r in res]
