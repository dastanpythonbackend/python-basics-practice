# 1) Запустите код примера со слайда Русско-английский словарь.
# Как видите, словарь отсортирован по ключам, т.е. пары в словаре
# идут в порядке возрастания по русскому алфавиту. Вот такое
# дополнение позволит отсортировать словарь по значениям
# (т.е. по англ. алфавиту в значениях):
# sorted_values = sorted(rusEng.values()) # отсортированный список значений
# engRus = {} # пустой будущий англо-русский словарь
# # в цикле пройти все значения (англ.слова); на каждом шаге
# находить соответствующее данному значению русское слово в
# ключах и помещать его в качестве ключа в пару к данному значению
# for i in sorted_values:
# for k in rusEng.keys():
# if rusEng[k] == i:
# engRus[k] = rusEng[k]
# break
# print(engRus) # вывод на экран получившегося словаря
# Дополните код таким образом, чтобы на выходе получался именно
# англо-русский словарь, т.е. поменяйте местами ключи и значения в словаре engRus.

rusEng = {
    'автомобиль': 'car',
    'дом': 'house',
    'кошка': 'cat',
    'собака': 'dog'
}

sorted_values = sorted(rusEng.values())

engRus = {}

for i in sorted_values:
    for k in rusEng.keys():
        if rusEng[k] == i:
            engRus[rusEng[k]] = k
            break
print(engRus)
