import re

pattern = r'(=)(\w{3})='
string = '=abc= =123= =def= 456 =fed= =321= =cba='

result = re.findall(pattern, string)

print(result) # [('=', 'abc'), ('=', '123'), ('=', 'def'), ('=', 'fed'), ('=', '321'), ('=', 'cba')]
