# Задача 7
# Создайте функцию, которая принимает на вход список
# чисел и возвращает среднее арифметическое
# всех элементов списка.

def calculate_average(nums):
    if len(nums) == 0:
        return 'Список не должен быть пустым'

    return sum(nums) / len(nums)


nums = [10, 20, 30, 40, 50]
average = calculate_average(nums)
print(f'Среднее арифметическое: {average}')
