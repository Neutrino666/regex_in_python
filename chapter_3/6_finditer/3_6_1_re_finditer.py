import re

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'

res = re.finditer(pattern, string)

for i in res:
    print(i)