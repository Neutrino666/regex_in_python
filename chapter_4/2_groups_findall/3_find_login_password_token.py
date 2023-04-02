import re

pattern = r'(\d+):(\w+):([a-z0-9]+)'
print(re.findall(pattern, input()))