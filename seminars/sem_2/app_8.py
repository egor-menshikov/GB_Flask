"""
Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""

from flask import Flask, flash, redirect, render_template, request, url_for
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.get('/')
def form_get():
    return render_template('form_name.html')

@app.post('/')
def form_post():


if __name__ == '__main__':
    app.run(debug=True)