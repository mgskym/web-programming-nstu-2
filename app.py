from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/menu")
def menu():
    return """
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
"""

@app.route("/lab1")
def lab1():
    return """
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
    </main>
    <footer>
        &copy; Маглицкий М, Овчинникова Ю, ФБИ-12, 3 курс, 2023
    </footer>
</body>
</html>
"""
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
    <h1>Дуб</h1>
    <img src="''' + url_for('static', filename='oak.jpg') + '''">
</body>
</html>
'''

@app.route("/lab1/student")
def student():
    return """
<!DOCTYPE html>
<html lang="ru">
<body>
    <main>
        Овчинникова Юлия Андреевна, Маглицкий Михаил Андреевич
        <img src="''' + url_for('static', filename='logo.jpg') + '''">
    </main>
</body>
</html>
"""
