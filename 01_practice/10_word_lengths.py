# Задача 10
# Создайте функцию, которая принимает на вход
# список слов и выводит на экран длину каждого слова.

def print_word_lengths(words):
    for word in words:
        print(f"Длина слова '{word}' = {len(word)}")


words = ['яблоко', 'банан', 'вишня', 'персик']
print_word_lengths(words)
