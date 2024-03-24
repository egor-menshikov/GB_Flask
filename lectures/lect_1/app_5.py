from collections import namedtuple

from flask import Flask
from flask import render_template

app = Flask(__name__)

User = namedtuple('User', 'name surname')


@app.route('/index/')
def html_index():
    _users = [User('Egor', ' Menshikov'), User('Sergei', 'Filimonov')]
    context = {'users': _users}
    return render_template('index2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
