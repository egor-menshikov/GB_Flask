from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    response.set_cookie('age', '38')
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    age = request.cookies.get('age')
    return f"Значение cookie: {name} , {age}"


if __name__ == '__main__':
    app.run(debug=True)
