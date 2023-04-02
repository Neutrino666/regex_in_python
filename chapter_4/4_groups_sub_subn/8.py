import re

if res := re.search(r'(\d+[₽|$])', input()):
    print(res.expand(r'Цена данного товара \1'))