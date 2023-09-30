from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')

@lab2.route("/lab2/defend")
def defend():
    # 1
    A = 3.1
    B = 5.7
    C = 12.8

    if A < B < C:
        A = A * 2
        B = B * 2
        C = C * 2
        result = A, B, C
    else:
        result = A, B, C
    return render_template('lab2defend.html', result = result)

@lab2.route("/lab2/example")
def example():
    lab_number = '2'
    name = 'Овчинникова Юля, Маглицкий Михаил'
    group = 'ФБИ-12'
    course = '3'
    cssPath = url_for('static', filename='lab1.css')
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'грушы', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]

    books = [
        {'author': 'Анджей Сапковский', 'name': 'Последнее желание', 'genre': 'Эпическое фентези', 'pages': 645},
        {'author': 'Джон Рональд Руэл Толкин', 'name': 'Властелин колец', 'genre': 'Роман-эпопея', 'pages': 1900},
        {'author': ' Джордж Р. Р. Мартин', 'name': 'Игра Престолов', 'genre': 'Фэнтези', 'pages': 1495},
        {'author': 'Стивен Кинг', 'name': 'Зелёная миля', 'genre': 'Мистика', 'pages': 735},
        {'author': 'Маргарет Митчелл', 'name': 'Унесённые ветром', 'genre': 'Роман', 'pages': 906},
        {'author': 'Антон Павлович Чехов', 'name': 'Вишнёвый сад', 'genre': 'Комедия', 'pages': 305},
        {'author': 'Дарья Донцова', 'name': 'Я очень хочу жить', 'genre': 'Иронический детектив', 'pages': 580},
        {'author': 'Амброз Бирс', 'name': 'Словарь Сатаны', 'genre': 'Сатира', 'pages': 479},
        {'author': 'Всеволод Михайлович Гаршин', 'name': 'Лягушка-путешественница', 'genre': 'Сказка', 'pages': 105},
        {'author': 'Алан Милн', 'name': 'Винни-Пух', 'genre': 'Фикшн', 'pages': 261}
    ]
    return render_template('example.html', name=name, lab_number=lab_number, cssPath=cssPath,
                           group=group, course=course, fruits=fruits, books=books)

@lab2.route("/lab2/bands")
def bands():
    return render_template('bands.html')

@lab2.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>
    <main>
    <h1>Меню</h1>
        <ul>
            <li><a href="/lab1">Первая лабораторная</a></li>
            <li><a href="/lab2">Вторая лабораторная</a></li>
        </ul>
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''