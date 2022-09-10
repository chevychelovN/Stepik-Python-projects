"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""

import re
import sys
reg = r"(\w)(\1+)"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(reg, r"\1", line))
    
