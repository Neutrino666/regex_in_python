import re

# Условие: Разделите строку по символам ? и &
# Пример ввода: https://www.youtube.com/results?search_query=random+stream&sp=EggIARABGAFAAQ%253D%253D

print(re.split(r'([?&])', input()))