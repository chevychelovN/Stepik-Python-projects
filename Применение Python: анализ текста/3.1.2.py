"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.
"""

s = input()
t = input()
count = 0
while s != "":
    if(s.startswith(t)):
        count += 1
    s = s[1:]

print(count)
