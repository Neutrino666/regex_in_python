import re

pattern = r'#\w*'
s = " #traveler #traveller #traveltheworld"

res = re.search(pattern, s)

if res:
    print(res[0])