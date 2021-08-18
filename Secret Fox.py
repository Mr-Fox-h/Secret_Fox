import random
from typing import Counter
# Init
Lower_C = "abcdefghijklmnopqrstuvwxyz"
Upper_C = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
Symbols = "[]{}()*;/,._-+\'\"?%/"
all = Lower_C + Upper_C + Numbers + Symbols
# Long pass
Counter = int(input("How many?: "))
Secret_Fox = "".join(random.sample(all, Counter))
print("Your password: " + Secret_Fox)
