from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.mydb

app.config.from_object('settings')

# @app.route('/')
# def index():
#   return render_template('customTemplate.html') # unction home() uses the Flask function render_template() to render the home.html template

# @app.route('/home')
# def home():
#   return render_template('home2.html')

# @app.route('/about')
# def about():
# 	return render_template('about2.html')

# @app.route('/contact')
# def contact():
# 	return render_template('contact2.html')

# @app.route('/myprofile')
# def profile():
# 	return render_template('myprofile.html')

# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')

# @app.route('/analysis')
# def analysis():
#     return render_template('analysis.html')            


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['inputEmail']
        password =request.form['inputPassword']
        print user
        print "*******************************"
        users = db.mycol2.find_one({'email': user})
        print users.get("email")
        print "*******************************" 
        if user != users.get("email"):
            error = 'Invalid username'
        elif password != users.get("password"):
            error = 'Invalid password'
        else:
            session[user] = users.get("email")
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('signIn.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

if __name__ == '__main__':
	app.debug = True
	app.run()
