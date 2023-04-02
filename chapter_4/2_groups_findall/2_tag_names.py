import re

pattern = r'(?:(?<=<)|(?<=</))(\w+).*?(?=>)'
result = re.findall(pattern, input())
print(result)