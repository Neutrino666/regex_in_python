import re

print(*re.findall(r'[\w-]+@[\w-]+\.(?:com|ru)', input()), sep='\n')