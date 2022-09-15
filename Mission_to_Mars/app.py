from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import mars_scrape


app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

@app.route('/')
def home():
    data = mongo.db.collection.find_one()
    return render_template('index.html', mars=data)

@app.route('/scrape')
def scrape():
    mars_data = mars_scrape()
    grab = mars_data.scrape()
    mongo.db.collection.update_one({}, {"$set": grab}, upsert=True)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)