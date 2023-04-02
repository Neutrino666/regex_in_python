import re


def del_word_info(word: re) -> str:
    return f'удалено({str(len(word[0]))})'


print(re.sub(r'\b[аА]\w*\b', del_word_info, input()))
