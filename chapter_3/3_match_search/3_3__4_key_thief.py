import re

pattern = r'\b(?<=Activation key: )(?:[A-Z0-9]{5}-){4}[A-Z0-9]{5}\b'

for _ in range(5):
    res = re.search(pattern, input())
    if res:
        print(res[0])
        break