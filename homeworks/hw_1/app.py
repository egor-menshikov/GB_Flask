from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def index():
    return render_template('base_template.html')


@app.route('/footwear/')
def footwear():
    return render_template('footwear.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

if __name__ == '__main__':
    app.run()
