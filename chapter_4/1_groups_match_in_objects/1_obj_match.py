import re

regex = r'П(?P<name>.+?)т' # Захватим весь текст между П и т в группу с именем name
text = 'Привет, как тебя зовут?'

match = re.match(regex, text)
# <re.Match object; span=(0, 6), match='Привет'>
print(match[0])
print(match[1])
# print(match[2]) # Ошибка: IndexError: no such group
print(match['name'])
print(match.group(0, 1, 'name'))
print(match.start(0))
print(match.end(0))
print(match.start(1))
print(match.end(1))
print(match.groups('Ничего не найдено')) # Задал default в случае None
# вернет кортеж всех групп кроме нулевой если ничего не то None
print(match.groupdict()) # {'name': 'риве'}