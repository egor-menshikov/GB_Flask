"""
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_name():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        count = len(request.form.get('sentence').split())
        return f'{sentence} <br>{count}'
    return render_template('form_name.html')


if __name__ == '__main__':
    app.run(debug=True)
