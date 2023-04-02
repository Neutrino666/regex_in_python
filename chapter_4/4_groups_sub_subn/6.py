import re

pattern = r'\b([Ее]го|[еЕ]ё|[иИ]х)\w+\b'
print(re.sub(pattern, r'\1', input()))