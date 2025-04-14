# 2. Напишите скрипт, который принимает у пользователя его имя. Если имя короче двух символов,
# скрипт должен вывести сообщение «Слишком короткое имя», если длиннее 50, то «Слишком длинное имя»,
# а если число символов от 2 до 50, то вывести сообщение с приветствием по имени.
# Функцию, возвращающую длину строки, найдите в интернете самостоятельно.

def greet_user(name):
    name_length = len(name)
    if name_length < 2:
        return 'Слишком короткое имя'
    elif name_length > 50:
        return 'Слишком длинное имя'
    else:
        return f'Привет, {name}'


user_name = input('Введите ваше имя: ')
message = greet_user(user_name)
print(message)
