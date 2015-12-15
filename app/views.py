
from flask import render_template, flash, redirect, url_for, json, request
from app import app
from .connection import db
# from .forms import LoginForm
# from .models import Customer
from werkzeug import secure_filename

import datetime

app.config.update(dict(  
    SECRET_KEY='development key'
))


@app.route('/')
def index():
  return render_template('basicTemplate.html') # unction home() uses the Flask function render_template() to render the home.html template

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_us')
def about_signedIn():
    return render_template('about2.html')    

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact_us')
def contact_signedIn():
    return render_template('contact2.html')    

@app.route('/myprofile')
def profile():
    return render_template('myprofile.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')         

@app.route('/signUp')
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

@app.route('/signup',methods=['POST'])
def signUp():
    error = None
    name = request.form['inputName']
    adress = request.form['inputAdress']
    organisationalNumber = request.form['inputOrganisationalNumber']
    contactNumber = request.form['inputContactNumber']
    #sector = request.form['inputIndustrySector']
    email = request.form['inputEmail']
    username = request.form['inputUserName']
    password = request.form['inputPassword']
    password2= request.form['inputPassword2']

    full_form = email and username and password and password2

    equal_passwords = (password == password2)

    if full_form:
       
        username_found=db.mycol2.find_one({"username": str(username)})
        print(username_found)

        if username_found != None:
            flash(u'That username is already taken, please choose another', 'error')
            return redirect(url_for('signUp'))
        if not(equal_passwords): 
            error ='The password are not matching'
            return redirect(url_for('signUp'))
        else:
            newCustomer = {"name": str(name), "adress":str(adress), "email": str(email), "organisationalNumber": str(organisationalNumber), "contactNumber": str(contactNumber), """sector: str(sector),""" "email":str(email), "username": str(username), "password": str(password), "date": datetime.datetime.utcnow()}

            custid = db.registry.insert(newCustomer)
            print custid
            collectionNewCustomer = db['Customer_'+str(custid)]
            
            newCollection = {"transactions": None, "clients": None}
            client_collection_id = db['Customer_'+str(custid)].insert(newCollection)

            collectionTransaction = collectionNewCustomer.transactions
            collectionClient = collectionNewCustomer.clients

            return redirect(url_for('signupcompleted'))
    else:
        error= 'The form is not correctly fulfilled'
        return redirect(url_for('signUp'))   

    #validate the received values
    # if full_form and equal_passwords:
    #     #for user in db.customer:
    #     #  print (user.username)
    #     #newCustomer = Customer(username, password)
    #     newCustomer = {"name": str(name), "adress":str(adress), "email": str(email), "organisationalNumber": str(organisationalNumber), "contactNumber": str(contactNumber), """sector: str(sector),""" "email":str(email), "username": str(username), "password": str(password), "date": datetime.datetime.utcnow()}

    #     #custid = customers.insert(newCustomer)
    

    # else:
    #     return json.dumps({'html':'<span>Enter the required fields</span>'})

    # validate the received values
    #if full_form:
        #for user in db.customer:
        #  print (user.username)
        #newCustomer = Customer(username, password)
        #newCustomer = {"email": str(email), "username": str(username),"password": str(password), "date": datetime.datetime.utcnow()}
        
        #db_empty=customers.find_one()
        #if db_empty!= None:
         #   x=customers.find_one({"username": str(username)})

        # if x!= None:
        #     flash("That username is already taken, please choose another")
        #     return render_template('signUp')
    #     if not(equal_passwords): 
    #         flash("The password are not matching")
    #         return render_template('signUp')
    #     else:
    #         newCustomer = {"name": str(name), "adress":str(adress), "email": str(email), "organisationalNumber": str(organisationalNumber), "contactNumber": str(contactNumber), """sector: str(sector),""" "email":str(email), "username": str(username), "password": str(password), "date": datetime.datetime.utcnow()}

    #         custid = customers.insert(newCustomer)
    #         return redirect(url_for('signupcompleted'))
    # else:
    #     flash("The form is not correctly fulfill")
    #     return render_template('signUp')    

       
        # newCustomer = Object()
        # newCustomer.name = str(name)
        # newCustomer.adress= str(adress)
        # newCustomer.organisationalNumber=str(organisationalNumber)
        # newCustomer.contactNumber = str(contactNumber)
        # newCustomer.sector = str(sector)
        # newCustomer.email=str(email)
        # newCustomer.username = str(username)
        # newCustomer.password= str(password)
        #cstid2 = customer.insert(newCustomer)
        #db.collection.insert(Customer(username, password)) 


# @app.route('/signIn',methods=['POST'])
# def signIn():
#     #email = request.form['inputEmail']
#     #password = request.form['inputPassword']  
#     # email = "poly@gmail.com"
#     # password = "pp"
#     customer= customers.find_one({"email": email, "password":password})

#     if customer == null : 
#       #return redirect(url_for('my_profile'))
#       return json.dumps({'html':'<span> Not Founded</span>'})
#     else:
#       return json.dumps({'html':'<span> Founded</span>'})
#       #return flash('Invalid authentication')
#       #return redirect(url_for('signin')) 

if __name__ == '__main__':
    app.debug = True
    app.run()

