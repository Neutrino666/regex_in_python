import re

pattern = r'<.+?>'

print(re.sub(pattern, '', input()))