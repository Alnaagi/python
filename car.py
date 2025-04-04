from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Flask app and database connection
app = Flask(__name__)
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

def scrape_bid_cars(search_query):
    try:
        # Initialize Selenium WebDriver
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Construct the search URL with the entered query for archived results
        url = f"https://bid.cars/en/search/archived/results?search-type=typing&query={search_query}&status=All&make=All&model=All&year-from=1900&year-to=2026&auction-type=All"
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)

        # Get the list of car titles (using the "item-title damage-info" class)
        car_titles = driver.find_elements(By.CLASS_NAME, "item-title.damage-info")
        # Get the final bid prices (using the "price-box" class)
        bid_prices = driver.find_elements(By.CLASS_NAME, "price-box")

        # Extract the titles and bid prices and store them in the database
        for i in range(len(car_titles)):
            title = car_titles[i].text
            try:
                price_text = bid_prices[i].text.strip()
                final_bid = price_text.split(':')[-1].strip()  # Get the price value after "Final bid:"
            except IndexError:
                final_bid = "No bid"
            
            # Save the data to the database
            car = Car(title=title, final_bid=final_bid)
            db.session.add(car)

        # Commit the session to save the data
        db.session.commit()

        return True  # Return True if scraping and saving to database was successful

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        driver.quit()

@app.route('/')
def index():
    # Fetch the car data from the database
    cars = Car.query.all()
    return render_template('table.html', cars=cars)

@app.route('/scrape')
def scrape():
    search_query = "335i"  # Set your search query here or accept user input
    success = scrape_bid_cars(search_query)

    if success:
        return "Scraping completed and data saved to database."
    else:
        return "An error occurred during scraping."

if __name__ == '__main__':
    app.run(debug=True)
