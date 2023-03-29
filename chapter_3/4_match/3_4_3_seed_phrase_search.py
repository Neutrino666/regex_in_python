import re

if re.search(r'\A[a-z]+(?: [a-z]+){11}(?= |$)', input()):
    print('возможно, это seed-фраза')
