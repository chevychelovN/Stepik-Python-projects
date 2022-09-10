"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
"""

import re
import sys
reg = r".*\\.*"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(reg, line):
        print(line)
        
