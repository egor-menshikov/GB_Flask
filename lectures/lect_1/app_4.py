
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Егор',
        'number': 5
    }
    return render_template('index1.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
