from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/code")
def code():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <script>
            console.log('hello!');
        </script>
    </body>
    </html>
'''