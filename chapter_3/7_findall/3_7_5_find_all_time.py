import re

pattern = r'\b(?:[01][0-9]|[2][0-3]):[0-5][0-9]\b'
print(*re.findall(pattern, input()), sep='\n')