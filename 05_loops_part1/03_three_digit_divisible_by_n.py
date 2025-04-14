# 3. Вывести все трёхзначные числа, кратные N, где N – число,
# введённое пользователем с клавиатуры.

def get_three_digit_multiples_of_n(n):
    for num in range(100, 1000):
        if num % n == 0:
            print(num)


user_input = int(input('Введите число: '))

get_three_digit_multiples_of_n(user_input)
