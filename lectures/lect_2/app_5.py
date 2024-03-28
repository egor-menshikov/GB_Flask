from flask import Flask, request, render_template

app = Flask(__name__)


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'


if __name__ == '__main__':
    app.run()
