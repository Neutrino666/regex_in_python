import re

pattern = r'\d{3}'
string = 'abc 123 def 456 fed 321 cba'
# Ищет только 1 вхождение, самое первое
result = re.search(pattern, string)

print(result)

result = re.search(r'\d{3}', 'abcdef')

print(result)
