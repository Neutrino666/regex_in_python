import re

# Пример ввода: *Курсив* и **Жирный текст**

pattern1 = r'(\*\*)([\w ]+)\1'
pattern2 = r'(\*)([\w ]+)\1'
res = re.sub(pattern1, r'<strong>\2</strong>', input())
res = re.sub(pattern2, r'<em>\2</em>', res)
print(res)