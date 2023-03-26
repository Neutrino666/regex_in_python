import re
from datetime import datetime


def timer(func):

    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        print(datetime.now() - start)
    return wrapper


@timer
def catastrophic_backtracking(n:int) -> None:
    re.findall(r'(a+)+b', 'a' * n)


if __name__ == '__main__':
    catastrophic_backtracking(29)
