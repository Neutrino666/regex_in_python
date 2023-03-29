import re

pattern = r'\A[A-Za-zА-Яа-яёЁ]+\b'
res = re.match(pattern, input())
if res:
    print(f'Первое слово в предложении: {res.group()}')
