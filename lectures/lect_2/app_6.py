from pathlib import PurePath, Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'


@app.get('/getfile')
def get_file():
    return render_template('file_form.html')


@app.post('/getfile')
def submit_post():
    if request.method == 'POST':
        file = request.files.get('upload_file')
        file_name = secure_filename(file.filename)
        print(file_name)
        file_path = PurePath.joinpath(Path.cwd(), 'uploads', file_name)
        file.save(file_path)
        file.close()

        with open(file_path, 'r', encoding='utf-8') as f:
            text = '\n'.join(f.readlines())
            print(type(text))
        return text


if __name__ == '__main__':
    app.run()
