import re

match = re.search(r'(\d{4})', 'Бойцовский клуб (1999)')
print(match.expand(r'Год выпуска фильма: \1'))    # Год выпуска фильма: 1999

