from flask import Flask, flash, redirect, render_template, request, url_for

# import secrets
#
# key = secrets.token_hex()
app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e'


@app.route('/form', methods=['GET', 'POST'])
def form():

    if request.method == 'POST':

        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))

        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))

    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
