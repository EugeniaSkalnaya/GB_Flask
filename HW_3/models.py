from flask_sqlalchemy import SQLAlchemy

HW_3 = SQLAlchemy()


class User(HW_3.Model):
    id = HW_3.Column(HW_3.Integer, primary_key=True)
    firstname = HW_3.Column(HW_3.String(80), nullable=False)
    lastname = HW_3.Column(HW_3.String(80), nullable=False)
    email = HW_3.Column(HW_3.String(80), nullable=False)
    password = HW_3.Column(HW_3.String(80), nullable=False)

    def __repr__(self):
        return f'{self.firstname} {self.surname}, {self.email}'
