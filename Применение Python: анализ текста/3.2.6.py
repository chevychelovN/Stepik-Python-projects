"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
"""

import re
import sys
reg = r".*\bcat\b.*"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub("human", "computer", line))
    
