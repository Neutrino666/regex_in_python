import re

# Example 1

pattern = r'[a-z]{3}'
replace = '111'
string = 'abc 123 def 456 fed 321 cba'

result = re.sub(pattern, replace, string)

print(result)

# Example 2

result = re.sub(pattern, replace, string, 2)
print(result)

# Example 3

pattern = r'[a-z]10_re_subn'

result = re.sub(pattern, replace, string)
print(result)