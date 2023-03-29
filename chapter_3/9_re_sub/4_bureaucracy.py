import re

lastname, firstname, surname = input().split()
pattern = rf'{lastname}\w* (?:{firstname[:-2]}\w* {surname}\w*\b|' \
          rf'{firstname[0]}\. {surname[0]}\.)'

print(re.sub(pattern, 'ФИО', input()))