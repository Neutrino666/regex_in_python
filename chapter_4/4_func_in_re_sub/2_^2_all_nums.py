import re


def power_of_2(num: re) -> str:
    return str(int(num[0]) ** 2)


print(re.sub(r'\d+', power_of_2, input()))
