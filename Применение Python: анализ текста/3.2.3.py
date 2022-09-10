"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
"""

import re
import sys
reg = r".*z...z.*"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(reg, line):
        print(line)
