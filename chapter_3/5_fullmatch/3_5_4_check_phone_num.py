# import re
#
# # pattern = r'(?:\+|)[1-8_re_split] ?(?:\([100-999]{3}\) ?|[100-999]{3} ?|[10_re_subn-99]{2} [0-9])'
# # pattern = r'\+?[1-8_re_split]'
# # +688 893 512 92 14
#
# patterns = [
#     r'\+?[1-8_re_split] ?(?:\(?[0-9]{3}\)?[0-9]{7,16}|\(?[0-9]{3}\)?[- ]?[0-9]{3}-[0-9]{2}-[0-9]{2})',
#     r'\+?[1-8_re_split] ?(?:\(?[0-9]{3}\)? ?[0-9]{3} ?[0-9]{2} ?[0-9]{2})',
#     r'\+?[100-999]{3} ?[0-9]{3} ?[0-9]{3} ?[0-9]{2} ?[0-9]{2}'
# ]
# ipt = input().replace(' ', '')
#
# for i, pattern in enumerate(patterns):
#     res = re.fullmatch(pattern, ipt)
#     if res:
#         print(True)
#         break
#     elif i + 1 == len(patterns):
#         print(False)
#

import re

patterns = [
    r'\+?[1-8_re_split](?:\(?[0-9]{3}\)?[0-9]{7,16}|\(?[0-9]{3}\)?-?[0-9]{3}-[0-9]{2}-[0-9]{2})',
]
ipt = input().replace(' ', '')

for i, pattern in enumerate(patterns):
    res = re.fullmatch(pattern, ipt)
    if res:
        print(True)
        break
    elif i + 1 == len(patterns):
        print(False)
