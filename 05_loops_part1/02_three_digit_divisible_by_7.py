# 2. Вывести все трёхзначные числа, кратные 7.

def get_three_digit_multiples_of_7():
    for num in range(100, 1000):
        if num % 7 == 0:
            print(num)


get_three_digit_multiples_of_7()
