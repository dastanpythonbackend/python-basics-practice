# 3. Напишите игру «Угадай число от 1 до 10»:
# В коде задано целое число от 1 до 10. Пока пользователь не введёт правильного ответа,
# программа запрашивает у него число на вход, а после того, как он угадал число, поздравляет его.

import random


def guess_the_number():
    secret_number = random.randint(1, 10)

    while True:
        user_guess = int(input('Угадайте число от 1 до 10: '))
        if user_guess < secret_number:
            print('Слишком мало! Попробуйте снова.')
        elif user_guess > secret_number:
            print('Слишком много! Попробуйте снова.')
        else:
            print(f'Поздравляю! Вы угадали число {secret_number}.')
            break


guess_the_number()
