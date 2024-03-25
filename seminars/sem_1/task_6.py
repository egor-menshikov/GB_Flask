"""Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст."""
from collections import namedtuple

from flask import Flask
from flask import render_template

app = Flask(__name__)

Student = namedtuple('Student', 'name surname age point_avg')


@app.route('/')
def index():
    context = {
        'students': [
            Student('Egor', 'Menshikov', '38', '100'),
            Student('Sergei', 'Filimonov', '36', '100'),
            Student('Varvara', 'Kirillina', '33', '100'),
        ]
    }
    return render_template('index6.html', **context)


if __name__ == '__main__':
    app.run()
