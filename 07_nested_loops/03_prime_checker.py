# 3. Напишите код, который описан на слайде № 4 про простые
# числа.

for N in range(2, 101):
    is_prime = True

    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break

    if is_prime:
        print(N)
