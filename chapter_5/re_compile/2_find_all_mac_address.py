import re

pattern = re.compile(r'(?:[A-F0-9]{2}:){5}[A-F0-9]{2}')

# Пример ввода: Мак-адрес моего друга:F0:98:9D:1C:93:F6. Мой мак-адрес: 0F:70:DE:55:60:19.
print(pattern.findall(input()))