# 5. Вывести все двузначные числа, которые превосходят произведение своих цифр.

def find_two_digit_numbers_greater_than_product():
    for num in range(10, 100):
        tens = num // 10
        units = num % 10
        product = tens * units
        if num > product:
            print(num)


find_two_digit_numbers_greater_than_product()
