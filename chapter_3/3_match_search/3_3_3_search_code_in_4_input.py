import re

pattern = r'\b[Кк]од\b'

res = object()

for i in range(1, 5):
    res = re.search(pattern, input())
    if res:
        print(f'{i} {res.start()}')
        break
    elif i == 4:
        print('код не найден')