import re

pattern = '[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]'

print(re.sub(pattern, '!', input()))