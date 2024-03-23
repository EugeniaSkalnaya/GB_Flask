import os
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from models import HW_3, User
from registration_form import RegisterForm
import hashlib

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HW_database.db'
HW_3.init_app(app)

#создаем базу данных
@app.cli.command("init-db")
def init_db():
    HW_3.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        salt = os.urandom(16)
        password_protection = password
        key = hashlib.pbkdf2_hmac('sha256', password_protection.encode('utf-8'), salt, 100000, dklen=128)
        user = User(firstname=firstname, lastname=lastname, email=email, password=key)
        HW_3.session.add(user)
        HW_3.session.commit()
        return "Регистрация прошла успешно"
    return render_template('register.html', form=form)


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
