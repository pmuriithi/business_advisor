import os
import json
import xlrd
import parse
import notify
import os.path
from xlrd import open_workbook
from flask import request, redirect, url_for,render_template, flash
from werkzeug import secure_filename


#where we store the uploaded file(use double slash to avoid the IOError22: invalid filename)
#UPLOAD_FOLDER =  'C:\\Users\\POLY\\Google Drive\\Desktop\\UPC\\BIP\\project\\temp\\test'
# UPLOAD_FOLDER = './test/'
#The file formats that are acceptable for upload
ALLOWED_EXTENSIONS = set(['xls','xlsx'])

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# app.config.update(dict(  
#     SECRET_KEY='development key'
# ))
#check that the uploaded file is in the right format in our case .xls or .xlsx.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

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

###########
#We then mapped the URL / to the function home(). Now, when someone visits this URL, the function home() will execute. 

	
# Python function finds a web template living in the templates/ folder.
#A web template will look in the static/ folder for any images, CSS, or JavaScript files it needs as it renders to HTML
#Rendered HTML is sent back to uploadtemp.py
#routes.py sends the HTML back to the browser	


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			parse.parse_file(filename)
			flash('Successfully uploaded %s' % filename)
			return redirect(url_for('upload_file'))
		else:
			flash('Invalid file %s' % file.filename)
			return redirect(url_for('upload_file'))			
	else:
		files = notify.get_files(UPLOAD_FOLDER)
		return render_template('upload.html', files=files)
		return redirect(url_for('upload_file'))
						
# if __name__ == '__main__':
# 	app.debug = True
# 	app.run()
