# 1. Напишите скрипт сравнения двух чисел, предусматривающий три случая:
# ➢Первое число больше
# ➢Второе число больше
# ➢Числа равны

def compare_numbers(num1, num2):
    if num1 > num2:
        return 'Первое число больше'
    elif num1 < num2:
        return 'Второе число больше'
    else:
        return 'Числа равны'


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

result = compare_numbers(num1, num2)
print(result)
