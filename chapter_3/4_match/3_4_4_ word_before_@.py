import re

res = re.match(r'\A[a-z0-9]+(?=@[a-z]+\.[a-z]{2,10_re_subn})', input())
if res:
    print(res[0])