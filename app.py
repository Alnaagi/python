from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Flask app and database connection
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_auction.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for storing car auction data
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    final_bid = db.Column(db.String(50), nullable=False)

# Initialize the database (only needs to be done once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    cars = Car.query.all()  # Fetch all cars from the database
    return render_template('table.html', cars=cars)

@app.route('/scrape')
def scrape():
    search_query = "335i"  # Set your search query here or accept user input
    print(f"Starting scrape for: {search_query}")
    success = scrape_bid_cars(search_query)

    if success:
        return "Scraping completed and data saved to database."
    else:
        return "An error occurred during scraping."

if __name__ == '__main__':
    app.run(debug=True)
