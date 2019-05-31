import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@myfirstcluster-lq5f8.mongodb.net/cookbook?retryWrites=true')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_cuisines')
def get_cuisines():
    return render_template("cuisines.html", 
                           cuisines=mongo.db.cuisines.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)