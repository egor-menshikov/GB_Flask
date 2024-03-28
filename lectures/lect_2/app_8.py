from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/redirect/')
def redirect_to_index():
    print('redir')
    return redirect('https://www.python.org/')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run()
