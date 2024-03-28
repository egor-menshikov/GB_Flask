"""
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""

from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.get('/')
def number_get():
    return render_template('form_num.html')

@app.post('/')
def number_post():
    

if __name__ == '__main__':
    app.run(debug=True)