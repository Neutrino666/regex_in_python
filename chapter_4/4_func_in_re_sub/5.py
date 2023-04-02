import re


def replacer(num: re) -> str:
    num = int(num[0])
    return f'{int(num / 3)}' if num > 0 and not num % 3 else str(num)


print(re.sub(r'\b\d+\b', replacer, input()))