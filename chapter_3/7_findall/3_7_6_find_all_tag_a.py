import re

pattern_tag_a = r'(?<=\<a).+?(?=\>)'
pattern_href = r'(?<=href=").+?(?=")'

results = re.findall(pattern_tag_a, input())

[print(re.search(pattern_href, string)[0], sep='\n') for string in results]