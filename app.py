# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os


# create instance of Flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

#initialize MongoDB

# Create route that renders index.html template and finds documents from mongo

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_info = mongo.db.mars_collection.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = scrape_mars.scrape_mars_news()
    mars_info = scrape_mars.scrape_mars_image()
    mars_info = scrape_mars.scrape_mars_facts()
    mars_info = scrape_mars.scrape_mars_weather()
    mars_info = scrape_mars.scrape_mars_hemispheres()
    mongo.db.mars_collection.update({}, mars_info, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)