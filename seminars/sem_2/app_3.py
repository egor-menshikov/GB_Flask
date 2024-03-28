"""
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""


from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def form_get():
    return render_template('form.html')

@app.post('/')
def form_post():
    return request.form.get('login') + '\n' + request.form.get('password')


if __name__ == '__main__':
    app.run(debug=True)