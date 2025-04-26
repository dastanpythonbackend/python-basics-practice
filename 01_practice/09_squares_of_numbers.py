# Задача 9
# Напишите программу, которая генерирует список всех
# квадратов целых чисел от 1 до 10.

def generate_squares():
    squares = [x ** 2 for x in range(1, 11)]
    return squares


squares = generate_squares()
print(squares)