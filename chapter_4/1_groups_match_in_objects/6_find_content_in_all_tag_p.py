import re

pattern = r'<p[^<]*?>.+?(?=\<\/p>)'
result = re.findall(pattern, input())

for res in result:
    print(res.split('>', 1)[1])