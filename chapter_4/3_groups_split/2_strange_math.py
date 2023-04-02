import re

pattern = r'[^+-:=*\d/]+'

print(re.split(pattern, input()))