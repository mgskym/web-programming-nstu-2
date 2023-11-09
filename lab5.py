from flask import Blueprint, render_template, request, redirect
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

    errors=[]


 

    if request.method=='GET':

        return render_template('register.html', errors=errors)

   

    username=request.form.get('username')

    password=request.form.get('password')


 

   

    if not (username or password):

        errors.append("please, fill the fields")

        print(errors)

        return render_template('register.html', errors=errors)


 

    conn=dbConnect()

    cur=conn.cursor()


 

    cur.execute("SELECT username From users where username='{username}';")

   

    if cur.fetchone() is not None:

        errors.append('the user already exists')

        dbClose(cur,conn)

        return render_template('register.html', errors=errors)

   

    cur.execute(f"INSERRT INTO users(username, password) VALUES ('{username}','{password}');")

    dbClose(cur,conn)


 

    return redirect('/lab5/login')