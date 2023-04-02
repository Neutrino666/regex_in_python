import re

pattern = r'([\d.]+:\d+)'
print(re.sub(pattern, r'http://\1', input()))
