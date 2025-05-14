from flask import Flask

app = Flask(__name__)


@app.route('/')
def first():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return f"""Человечество вырастает из детства.</br>
    Человечеству мала одна планета.</br>
    Мы сделаем обитаемыми безжизненные пока планеты.</br>
    И начнем с Марса!</br>
    Присоединяйся!
    <span style="font-size: smaller;">
    У нас есть кофе и печеньки!</span>
"""


@app.route('/image_mars')
def image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/OIP.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <h6>Вот она какая, красная планета.</h6>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
