"""
Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя.
Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел.
Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""

def primes():
    a = 2
    while True:
        isPrime = True
        for j in range(2, a):
            if a % j == 0:
                isPrime = False
                break
        if isPrime:
            yield a
        a += 1
        
