from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class SignUpForm(Form):
    username = StringField('name', validators=[DataRequired()])
    password = BooleanField('password', validators=[DataRequired()])
    password2 = BooleanField('password2', validators=[DataRequired()])
