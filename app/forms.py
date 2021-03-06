from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

# class SignUpForm(Form):
#     username = StringField('name', validators=[DataRequired()])
#     password = BooleanField('password', validators=[DataRequired()])
#     password2 = BooleanField('password2', validators=[DataRequired()])

# class RegistrationForm(Form):
#     username = TextField('Username', [validators.Length(min=4, max=20)])
#     email = TextField('Email Address', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password', [
#         validators.Required(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
    

