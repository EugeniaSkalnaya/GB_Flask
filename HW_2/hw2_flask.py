# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# также будет произведено перенаправление на страницу приветствия, где будет
# отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую
# будет удалён cookie-файл с данными пользователя и произведено перенаправление
# на страницу ввода имени и электронной почты.
from flask import Flask, request, make_response, render_template, redirect
from markupsafe import escape

app = Flask(__name__)


@app.route('/index_hw/', methods=['GET', 'POST'])
def index_hw():
    username = request.cookies.get('username')
    if request.method == 'POST':
        response = make_response(redirect('/authorisation_new/'))
        response.delete_cookie('username')
        response.delete_cookie('email')
        return response
    return render_template('index_hw.html', username=username)


@app.route('/authorisation_new/', methods=['GET', 'POST'])
def authorisation_new():
    if request.method == 'POST':
        username = escape(request.form.get('auth_username'))
        email = escape(request.form.get('auth_email'))
        response = make_response(redirect('/index_hw/'))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    return render_template('authorisation_new.html')


if __name__ == '__main__':
    app.run(debug=True)
