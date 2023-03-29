import re

pattern = r'(?:(?:(?:\d{2}\.){2}|(?:\d{2}/){2})\d{4})|(?:\d{4}(?:(?:\.\d{2})){2}|\d{4}(?:(?:/\d{2}){2})'

print(*re.findall(pattern, input()), sep='\n')