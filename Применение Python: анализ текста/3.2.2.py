"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
"""

import re
import sys
reg = r".*\bcat\b.*"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(reg, line):
        print(line)
