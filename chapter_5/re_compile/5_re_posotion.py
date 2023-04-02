import re

#  Пример ввода
# soda senior tuition library task tone few torch vacuum
# 2
# 29

text, pos, endpos = input(), int(input()), int(input())

pattern = re.compile(r'\b\w+\b')

if res:= pattern.search(text, pos, endpos):
    print(res[0])
