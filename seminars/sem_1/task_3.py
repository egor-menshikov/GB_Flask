"""
Задание №3
Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/numbers/<int:a>/<int:b>/')
def numbers(a, b):
    return str(a + b)


if __name__ == '__main__':
    app.run()
