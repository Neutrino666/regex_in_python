import re

pattern = r'(\w+) \1'

print(re.sub(pattern, r'\1', input()))