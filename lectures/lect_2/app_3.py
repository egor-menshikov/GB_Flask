from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('about.html')


@app.route('/about/')
def about():
    context = {
        'title': 'Обо мне',
        'name': 'Егор',
    }
    return render_template('about.html', **context)


@app.route('/demo')
def demo():
    return render_template('demo.html')


if __name__ == '__main__':
    app.run()
