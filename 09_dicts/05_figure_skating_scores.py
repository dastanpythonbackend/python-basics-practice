# 5. На вход программе подаются результаты
# судейства по фигурному катанию. В первой
# строке N - количество участников и
# S - количество судей, разделённые пробелом,
# во второй - фамилии спортсменов через
# запятую с пробелом, в последующих N
# строках – S оценок судей в виде числа
# с плавающей точкой от 0.0 до 6.0. На экран
# нужно вывести фамилии спортсменов, занявших
# по итогу соревнований 1, 2 и 3 места, и их
# средний балл. Дроби округлить до второго
# знака после запятой.

# Пример ввода
# 4 3
# Асланова Иванова Петренко Ким
# 5.5 5.8 4.9
# 5.2 5.3 5.2
# 6.0 6.0 6.0
# 5.4 5.3 5.1
# Пример вывода
# Петренко 6.00
# Асланова 5.40
# Ким 5.27

def calculate_scores():
    n, s = map(int, input('Введите количество участников и судей: ').split())
    athletes = input('Введите фамилии спортсменов через запятую: ').split(',')
    scores = []

    for i in range(n):
        marks = list(map(float, input(f'Введите оценки для {athletes[i]}: ').split()))
        average_score = sum(marks) / s
        scores.append({'athlete': athletes[i], 'score': round(average_score, 2)})

    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)

    top_athletes = sorted_scores[:3]
    for athlete in top_athletes:
        print(f'{athlete['athlete']} {athlete['score']:.2f}'.strip())


calculate_scores()
