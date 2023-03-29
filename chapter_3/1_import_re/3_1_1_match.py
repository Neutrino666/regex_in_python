import re

regex = r'П.+?т'
text = 'Привет, как тебя зовут?'

match = re.match(regex, text)
print(match)
print(match.group())
print(match.group(0))
print(match[0])
print(match[0][0])
print(match.start(0))
print(match.end(0))
print(match.start(0))
print(match.end(0))
print(match.span(0))
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)