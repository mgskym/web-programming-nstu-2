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
    return conn

def dBClose(cursor,connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5')
def main():
    visibleUser = "Anon"
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "Julia_knowledge_base",
        password = "123"
    ).encode('UNICODE')

    cur = conn.cursor()
    cur.execute("SELECT * FROM users;").encoding('latin-1')

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return "go to console"