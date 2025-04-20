# 4. Подумайте, как его улучшить – до какого числа имеет смысл
# продолжать поиск делителя? Найдите первые 10 простых чисел
# после 100000000 (это 10 ** 10, или 10 миллиардов).

import math


def is_prime(N):
    if N <= 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(N)) + 1, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False
    return True


def find_primes_after_num(start, count):
    primes = []
    num = start
    while len(primes) < count:
        num += 1
        if is_prime(num):
            primes.append(num)
    return primes


start_num = 10**10
prime_num = find_primes_after_num(start_num, 10)

print(f'Первые 10 простых чисел после 10 миллиардов: {prime_num}')
