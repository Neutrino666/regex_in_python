import re

strings = [
    'يحتاج الجسم القوي إلى عقل قوي.',
    'Recognition is the most powerful motivation factor.',
    'Máme otevřeno 24 hodin denně.',
    '這個理論有一個缺點。',
    'Бездә бәхәссез дәлил бар.',
    '1234567890_+'
]

for s in strings:
    res = re.finditer(r'\w+', s)
    if res:
        for r in res:
            print(r[0])