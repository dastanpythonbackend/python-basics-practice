# 4. Вывести сумму цифр числа, полученного с клавиатуры.

def sum_of_digits(num):
    total = 0
    for digit in str(abs(num)):
        total += int(digit)
    return total


user_num = int(input('Введите число: '))
result = sum_of_digits(user_num)
print(f'Сумма цифр: {result}')
