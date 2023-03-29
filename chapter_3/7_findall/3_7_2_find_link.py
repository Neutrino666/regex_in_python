import re

pattern = r'https://imgur.com/[a-zA-Z0-9]{7}'
res = re.findall(pattern, input())
[print(r) for r in res if res]