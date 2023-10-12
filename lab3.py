from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/form1')
def form():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле'
    age =  request.args.get('age')
    sex =  request.args.get('sex')
    return render_template('lab3.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    drink = request.args.get('drink')
    milk = request.args.get('milk')
    sugar = request.args.get('sugar')
    return render_template('order.html', drink=drink, milk=milk,sugar=sugar)

@lab3.route('/lab3/pay')
def pay():
    price=0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price=120
    elif drink == 'black tea':
        price=80
    else:
        price=70

    if request.args.get('milk') == 'on':
        price+=30
    if request.args.get('sugar') == 'on':
        price +=10
    
    
    card = request.args.get('card')
    name = request.args.get('name')
    cvv = request.args.get('cvv')
    
    return render_template('pay.html', price=price, card=card, name=name, cvv=cvv)

@lab3.route('/lab3/success')
def success():
    return render_template('lab3pay.html')
    

@lab3.route('/lab3/ticket')
def ticket():
    errors={}
    user = request.args.get('user')
    if user == '':
         errors['user'] = 'Заполните поле'
    age =  request.args.get('age')
    if age == '':
         errors['age'] = 'Заполните поле'
    exit_point =  request.args.get('exit_point')
    if exit_point == '':
         errors['exit_point'] = 'Заполните поле'
    destination =  request.args.get('destination')
    if destination == '':
         errors['destination'] = 'Заполните поле'
    date =  request.args.get('date')
    if date == '':
         errors['date'] = 'Заполните поле'
    return render_template('ticket.html',  user=user, age=age, exit_point=exit_point,destination=destination,date=date, errors=errors)


#@lab3.route('/lab3/successticket')
#def successticket():
    #return render_template('lab3.successticket.html')