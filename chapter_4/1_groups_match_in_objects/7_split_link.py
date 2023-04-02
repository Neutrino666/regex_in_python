import re

pattern = r'\b(?P<protocol>http[s]?)://' \
          r'(?P<domain>[\w.]+?(com|org|ru))[\w/-]*' \
          r'(?P<param>\?[^ #]+)?(?P<anchor>#[\w]+)?'

result = re.finditer(pattern, input())

for res in result:
    print(f'Полная ссылка: {res[0]}')
    print(f'Протокол: {res.group("protocol")} | Домен: {res.group("domain")} | '
          f'Параметры: {res.group("param")} | Якорь: {res.group("anchor")}\n')