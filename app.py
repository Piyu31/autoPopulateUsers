from flask import Flask, render_template, redirect, request
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'thisissecretqwerty'
csrf.init_app(app)


client = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/mydatabase?retryWrites=true&w=majority')
db = client.mydatabase

collection = db.user
@app.route("/")
def finduser():
    x=list(collection.find({}))
    return render_template("viewUsers.html",x=x)

@app.route('/')
def main():
#redirect to userlist page!
    return render_template('viewUsers.html') 

@app.route('/profiles/<string:email>',methods = ['GET','POST'])
def profiling(email):
#redirect to edit page!
    user = collection.find_one({"email":email })
    return render_template('Edit.html',user=user)


#registration page
@app.route('/register/', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form['action'] == 'Register':
                #collect data from form to submit to database
                collection.update({'user_id': request.values.get('user_id')},
	            { '$set': { "first_name" :request.values.get('firstname'),"middlename_name" : request.values.get('middlename'),"last_name" : request.values.get('lastname'),"business_loc" :request.values.get('bunit'),"position" : request.values.get('pos'),"phone" : request.values.get('phone')}})	   
                flash('Registration Complete!','flashok')
                return redirect(url_for('register'))
                
		        # "first_name" :request.values.get('firstname'),
                # "middlename_name" : request.values.get('middlename'),
	            # "last_name" : request.values.get('lastname'),
		        # "business_loc" :request.values.get('bunit'),
                # "position" : request.values.get('pos'),
		        # "phone" : request.values.get('phone')
		        
                #insert into database collection		 collection.insert(newuser)
        


if __name__ == "__main__":
      app.config.update(
      DEBUG = True,
      CSRF_ENABLED = True,
      SECRET_KEY = 'adsfhjkaldhfhehh38718y2h2')
      app.run(host='104.131.27.56',port=5023)