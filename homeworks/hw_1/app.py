from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base_template.html')


@app.route('/footwear/')
def footwear():
    return render_template('footwear.html')


if __name__ == '__main__':
    app.run()
