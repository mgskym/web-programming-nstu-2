from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dBConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "julia_knowledge_base",
        password = "123",
        port = 5432
)
    return conn;

def dBClose(cursor,connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5')
def main():
    visibleUser = "Anon"
    visibleUser = session.get("username")
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "julia_knowledge_base",
        password = "123",
        port = 5432
)
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return render_template('lab5.html', username = visibleUser)

@lab5.route('/lab5/users')
def user():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "julia_knowledge_base",
        password = "123",
        port = 5432
)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('lab5users.html', users=result)



@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors = ""
    if request.method=='GET':
        return render_template('register.html', errors=errors)
    username=request.form.get('username')

    password=request.form.get('password')
    if not (username and password):
    
        errors = []
        errors = "Заполните все поля"
        print(errors)
        return render_template('register.html', errors=errors)
    hashPassword = generate_password_hash(password)
    conn=dBConnect()
    cur=conn.cursor()
    cur.execute(f"SELECT username From users where username='{username}';")

    if cur.fetchone() is not None:
        errors = 'the user already exists'
        
        conn.close()
        cur.close()
        return render_template('register.html', errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")
    conn.commit()
    conn.close()
    cur.close()
    return redirect('/lab5/login')


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def loginPage():
    errors = []
    if request.method=='GET':
        return render_template('login.html', errors=errors)

    username=request.form.get('username')
    password=request.form.get('password')

    if not (username and password):
    
        errors = []
        errors = "Заполните все поля"
        print(errors)
        return render_template('login.html', errors=errors)

    conn=dBConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT id, password From users where username='{username}';")
    result = cur.fetchone()

    if result is None:
        errors = []
        errors = 'Непавильный логин или пароль'
        
        dBClose(cur,conn)
        return render_template('login.html', errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
            session['id'] = userID
            session['username'] = username
            dBClose(cur,conn)
            return redirect ("/lab5")

    else:
            errors.append("Неправильный логин или пароль")
            return render_template("login.html", errors=errors)



@lab5.route('/lab5/new_article', methods=['GET', 'POST'])


 

def createArticle():
    errors = []
    userID = session.get("id")

    if userID is not None:
        if request.method=='GET':
            return render_template('note.html')

    
        if request.method=='POST':
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len('text_article') == 0:
                errors.append ("Заполните поле")
                return render_template('note.html', errors=errors)

            conn = dBConnect()
            cur = conn.cursor()
            cur.execute(f"INSERT INTO articles(user_id,title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")

        
            new_article_id = cur.fetchone()[0]
            conn.commit()
            dBClose(cur,conn)
            return redirect(f"/lab5/articles/{new_article_id}")

        return redirect ("/lab5/login")