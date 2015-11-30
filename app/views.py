
from flask import render_template, flash, redirect, json, request
from app import app
from app import db
from app import models
from .forms import LoginForm
from werkzeug import secure_filename

@app.route('/')
def index():
  return render_template('basicTemplate.html') # unction home() uses the Flask function render_template() to render the home.html template

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
  return render_template('upload.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/myprofile')
def profile():
    return render_template('myprofile.html')    

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for username="%s", password=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('signin.html', 
                           title='Sign In',
                           form=form)

@app.route('/signUp',methods=['POST'])
def signUp():
    # create user code will be here !!
     # read the posted values from the UI
    _username = request.form['inputUserName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _password2= request.form['inputPassword2']

    # validate the received values
    if _username and _password and _password2:
    
        newCustomer = models.Customer(username = _username, password = _password)
        newCustomer.save(); 
        
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
    return redirect('signupcompleted.html', 
                           title='Sign Up Completed',
                           form=form)

@app.route('/showSignUp')
def showSignUp():
    return redirect(url_for('signUp'))

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
 
    except Exception as e:
        return render_template('error.html',error = str(e))

