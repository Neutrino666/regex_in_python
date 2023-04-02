import re


def func(m: re) -> str:
    return str(len(m[0]))


reqex = r'[a-zA-Z]+'
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'

res_func = re.sub(reqex, func, text)
res_lambda = re.sub(reqex, lambda m: str(len(m[0])), text)

print(res_func)  # 5 5 2 6 5 4 2 3 8 3 11 8.
print(res_func == res_lambda)  # True