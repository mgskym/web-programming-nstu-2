from flask import Blueprint, render_template, request
lab4=Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'julia' and password == '1':
        return render_template('success.html')
    error = 'Неверные логин и/или пароль'
    if username == '':
        error='Вы не ввели логин'
    if password == '':
        error='Вы не ввели пароль'

    return render_template('login.html',error=error,
                           username=username, password=password)

    