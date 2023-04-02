import re


def replace_am_pm(am_or_pm: re) -> str:
    return 'am' if am_or_pm[0] == 'pm' else 'pm'


print(re.sub(r'((?<=\d)|(?<=\b))am|pm\b', replace_am_pm, input()))
