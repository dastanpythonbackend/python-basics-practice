# 4. Определить количество повторов слов во входной строке.
# Ввод: строка текста, в которой слова разделяются строго
# одним пробелом.
# Вывод: строки, каждая из которых состоит из слова и
# количества повторений для каждого из них. Строки
# должны быть отсортированы по убыванию встречаемости.
# Пример ввода:
# миллион миллион миллион алых роз
# Пример вывода:
# миллион 3
# алых 1
# роз 1

from collections import Counter


def count_word_reapeats(text):
    words = text.split()

    word_counts = Counter(words)

    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_counts:
        print(f'{word}: {count}')


input_text = input('Введите строку: ')
count_word_reapeats(input_text)
