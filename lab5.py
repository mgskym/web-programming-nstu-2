from flask import Blueprint, render_template, request, redirect
import psycopg2


lab5 = Blueprint('lab5', __name__)

@lab5.route("/lab5")
def main():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base_for_michael",
        user = "Michael_knowledge_base",
        password = "001914"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return "go to console"

   