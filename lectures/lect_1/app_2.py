from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return 'Привет, ' + name + '!'


@app.route('/file/<path:file>/')
def set_path(file):
    with open(file, 'r', encoding='utf-8') as f:
        result = f.readlines()
    return result


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run(debug=True)
