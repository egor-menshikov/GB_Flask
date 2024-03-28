"""
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_name_age():
    if request.method == 'POST':
        username = request.form.get('name')
        age = request.form.get('age')
        if int(age) >= 18:
            return f'{username} {age}'
        else:
            return 'Вы не проходите.'
    return render_template('form_name_age.html')


if __name__ == '__main__':
    app.run(debug=True)