# 2) Создать список из 5 элементов, заполняемый целыми числами с клавиатуры.
# Отсортировать его.

def create_and_sort_list():
    nums = []

    for i in range(5):
        num = int(input(f'Введите целое число №{i + 1}: '))
        nums.append(num)

    nums.sort()

    print(f'Отсортированный список: {nums}')


create_and_sort_list()
