# 1. Создайте новый проект PyCharm и файл celsius.py в нём

# 2. Создайте функцию, которая принимает на вход дробное значение градусов
# Цельсия и возвращает значения в градусах Фаренгейта и Кельвинах. Формула перевода:
# 𝐹 = 𝐶 ∙ 1.8 + 32
# 𝐾 = 𝐶 + 273.15

def convert_celsius(c):
    f = c * 1.8 + 32
    k = c + 273.15
    return f, k


result = convert_celsius(45)
print(result)

# 3. Протестируйте запуск скрипта средствами PyCharm и терминала.
