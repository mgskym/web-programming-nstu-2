from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Маглицкий М, Овчинникова Ю</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
        </ul>
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Маглицкий М, Овчинникова Ю</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        <br>
        <a href="http://127.0.0.1:5000/menu">Меню</a>
        <br>
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak</a> - Дуб</li>
            <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student</a> - Студент</li>
            <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python</a> - Python</li>
            <li><a href="http://127.0.0.1:5000/lab1>/lab1/</a> - </li>
        </ul>
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''
@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)

@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        Овчинникова Юлия Андреевна, Маглицкий Михаил Андреевич
        <br>
        <img style="width: 420px" src="''' + url_for('static', filename='logo.png') + '''">
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''
@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        Высокоуровневый язык программирования общего назначения с динамической строгой типизацией
        и автоматическим управлением памятью, ориентированный на повышение производительности
        разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных
        на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё
        является объектами. Необычной особенностью языка является выделение блоков кода пробельными
        отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает
        необходимость обращаться к документации.
        <br>
        <img style="width: 600px" src="''' + url_for('static', filename='pyt.jpg') + '''">
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</bodfly>
</html>
'''