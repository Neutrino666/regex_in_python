import re

# Example 1
pattern = r'\s\d{3}\s'
string = 'abc 123 def 456 fed 321 cba'

result = re.split(pattern, string)

print(result)

# Example 2

result = re.split(pattern, string, 2)
print(result)

# Example 2

pattern = r'123'
string = '456'

result = re.split(pattern, string)
print(result)