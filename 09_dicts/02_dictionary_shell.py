# 2) Составьте программу-оболочку для словаря со следующим функционалом:
# 1. Вывести английский перевод по введённому русскому слову;
# 2. Вывести русский перевод по введённому английскому слову;
# 3. Добавить слово и его перевод в словарь.
# Для каждого действия, если оно невозможно, должно быть
# предусмотрено сообщение об ошибке.

def dictionary_shell():
    dictionty = {
        'кот': 'cat',
        'собака': 'dog',
        'дом': 'house',
        'яблоко': 'apple'
    }

    while True:
        print('\nВыберите действие:')
        print('1 - Найти английский перевод по русскому слову')
        print('2 - Найти русский перевод по английскому слову')
        print('3 - Добавить новое слово')
        print('0 - Выйти')

        choise = input('Ваш выбор: ')

        if choise == '1':
            russian_word = input('Введите русское слово: ').lower()
            if russian_word in dictionty:
                print(f'Английский перевод: {dictionty[russian_word]}')
            else:
                print('Слово не найдено в словаре.')

        elif choise == '2':
            english_word = input('Введите английское слово: ').lower()
            found = False
            for rus, eng in dictionty.items():
                if eng == english_word:
                    print(f'Русский перевод: {rus}')
                    found = True
                    break
            if not found:
                print('Слово не найдено в словаре.')

        elif choise == '3':
            russian_word = input('Введите новое русское слово: ').lower()
            english_word = input('Введите его английский перевод: ').lower()
            if russian_word not in dictionty:
                dictionty[russian_word] = english_word
                print('Новое слово добавлено!')
            else:
                print('Такое русское слово уже есть в словаре.')

        elif choise == '0':
            print('Выход из программы.')
            break

        else:
            print('Неверный выбор. Попробуйте снова.')


dictionary_shell()
