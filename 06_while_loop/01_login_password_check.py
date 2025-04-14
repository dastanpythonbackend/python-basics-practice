# 1. Напишите код.
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# while login != 'meadmin' or password != 'adminpass':
# print('Неверный логин и/или пароль, попробуйте ещё')
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# print('Добро пожаловать!’)

login = input('Введите логин: ')
password = input('Введите пароль: ')
while login != 'meadmin' or password != 'adminpass':
    print('Неверный логин и/или пароль, попробуйте ещё')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    print('Добро пожаловать!')
