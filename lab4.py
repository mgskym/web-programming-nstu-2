from flask import Blueprint, render_template, request
import math
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username=request.args.get('username')
    password=request.args.get('password')
    error=''
    if username and password:
        if username == 'alex' and password == '123':
            return render_template('success.html')
        else:
            error = 'Неверные логин/пароль'
    return render_template('login.html', error=error, username=username, password=password)
    