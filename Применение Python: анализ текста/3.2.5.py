"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
"""

import re
import sys
reg = r".*\b(\w+)\1\b.*"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(reg, line):
        print(line)
