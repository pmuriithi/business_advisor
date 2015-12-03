
from flask import render_template, flash, redirect, url_for, json, request
from app import app
from .connection import db, customers
from .forms import LoginForm
from .models import Customer
from werkzeug import secure_filename

import datetime

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

@app.route('/signup')
def signup():
    return render_template('signUp.html') 

@app.route('/signupcompleted')
def signupcompleted():
    return render_template('signUpCompleted.html')   

@app.route('/signin')
def signin():
    return render_template('signIn.html')   
# index view function suppressed for brevity

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for username="%s", password=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('signin.html', 
#                            title='Sign In',
#                            form=form)

@app.route('/signUp',methods=['POST'])
def signUp():
   
    name = request.form['inputName']
    adress = request.form['inputAdress']
    organisationalNumber = request.form['inputOrganisationalNumber']
    contactNumber = request.form['inputContactNumber']
    sector = request.form['inputIndustrySector']
    email = request.form['inputEmail']
    username = request.form['inputUserName']
    password = request.form['inputPassword']
    password2= request.form['inputPassword2']

    full_form = email and username and password and password2

    equal_passwords = (password == password2)
    # validate the received values
    if full_form and equal_passwords:
        #for user in db.customer:
        #  print (user.username)
        #newCustomer = Customer(username, password)
        newCustomer = {"email": str(email), "username": str(username),"password": str(password), "date": datetime.datetime.utcnow()}
        custid = customers.insert(newCustomer)
        #db.collection.insert(Customer(username, password)) 

        return redirect(url_for('signupcompleted'))
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/signIn',methods=['POST'])
def signIn():
    email = request.form['inputEmail']
    password = request.form['inputPassword']  
 
    customer= customers.find_one({"email": email, "password":password})

    if customer: 
      #return redirect(url_for('my_profile'))
      return json.dumps({'html':'<span>Founded</span>'})
    else:
      #return json.dumps({'html':'<span>Not Founded</span>'})
      return flash('Invalid authentication')
      return redirect(url_for('signin')) 
   

