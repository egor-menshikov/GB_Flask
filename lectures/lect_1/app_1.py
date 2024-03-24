from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/egor/')
def hello_egor():
    return ('Hello Egor!')


@app.route('/egor')
def hello_egor2():
    return 'Hello Egor2!'


if __name__ == '__main__':
    app.run()
