from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/lab2/example")
def example():
    lab_number = '2'
    name = 'Овчинникова Юля, Маглицкий Михаил'
    group = 'ФБИ-12'
    course = '3'
    cssPath = url_for('static', filename='lab1.css')
    return render_template('example.html', name=name, lab_number=lab_number, cssPath=cssPath, group=group, course=course)

@app.route("/menu")
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
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        <h1>Лабораторная работа №1</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
        <br>
        <a class="btn" style="color: #fff; margin-bottom: 56px" href="http://127.0.0.1:5000/menu">Меню</a>
        <br>
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak</a> - Дуб</li>
            <li><a href="http://127.0.0.1:5000/lab1/student">/lab1/student</a> - Студент</li>
            <li><a href="http://127.0.0.1:5000/lab1/python">/lab1/python</a> - Python</li>
            <li><a href="http://127.0.0.1:5000/lab1/stress">/lab1/stress</a> - Стресс</li>
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
<head>
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
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
<head>
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        <p>
            Высокоуровневый язык программирования общего назначения с динамической строгой типизацией
            и автоматическим управлением памятью, ориентированный на повышение производительности
            разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных
            на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё
            является объектами. Необычной особенностью языка является выделение блоков кода пробельными
            отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает
            необходимость обращаться к документации.
        </p>
        <br>
        <img style="width: 600px" src="''' + url_for('static', filename='pyt.jpg') + '''">
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''

@app.route("/lab1/stress")
def stress():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet", type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>
    <main>
        <p>
            Достижения научно-технического прогресса, ускоренный ритм жизни требуют больше ментальных усилий.
            Захлестывающие информационные потоки, стремительное изменение социума, растущая многозадачность
            оборачиваются постоянным напряжением, что истощает психические и физические ресурсы. Чтобы выстоять
            в стрессовых условиях, многие начинают прием антидепрессантов, транквилизаторов, которые не лишены
            побочных эффектов. Психологи рекомендуют более безопасные, но при этом эффективные методы
            поддержания психофизиологического состояния. О том, как бороться со стрессом без вреда
            для здоровья, расскажем в статье.
        </p>
        <p>
            Понятие «стресс» было введено в медицину в начале прошлого века американским физиологом У. Кэнноном.
            Одним емким словом врач обозначил неспецифический адаптационный ответ организма на нервно-психические
            перегрузки. В послевоенные годы исследования Кэннона продолжил его ученик (канадский эндокринолог Г.
            Селье), а к концу XX столетия изучение стрессовых состояний и их последствий приобрело всемирный
            масштаб.
        </p>
        <p>
            Стресс может быть как позитивным, так и негативным. В первом случае это эустресс — яркое
            положительное событие, которое проходит без осложнений для организма, заряжает позитивом,
            завершается расслаблением. Во втором случае речь идет о дистрессе — длительном напряжении
            нервной системы, накоплении отрицательных эмоций. Подобное состояние негативно сказывается
            на всем организме, что обусловлено тесной связью психического компонента с соматическим.
            Перманентный стресс часто приводит к психоэмоциональным дисфункциям, аддикциям, развитию
            хронических заболеваний.
        </p>
        <br>
        <img style="width: 600px" src="''' + url_for('static', filename='kitten.jpg') + '''">
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
'''