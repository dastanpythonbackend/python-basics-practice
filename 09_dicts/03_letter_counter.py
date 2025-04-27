# 3) Напишите генератор словаря, который будет получать
# на вход строку из маленьких английских букв и записывать
# в качестве ключа букву, а в качестве значения – количество
# этих букв в исходной строке.
# Пример
# Вход: abadfdsfasb
# Выход: {'a': 3, 'b': 2, 'd': 2, 'f': 2, 's': 2}

def count_letters(string):
    return {letter: string.count(letter) for letter in set(string)}


input_string = input('Введите строку: ')
result = count_letters(input_string)
print(result)
