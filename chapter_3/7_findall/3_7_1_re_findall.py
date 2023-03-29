import re

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'

res = re.findall(pattern, string)

print(res) # ['123', '456', '321']
