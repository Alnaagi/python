from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Flask + DB setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    final_bid = db.Column(db.String(50), nullable=False)
    car_milage = db.Column(db.String(50), nullable=False)
    car_damage = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

def scrape_bid_cars(search_query):
    try:
        print("Initializing the WebDriver...")
        options = webdriver.ChromeOptions()
        # Run in headless mode for Render's environment
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("WebDriver initialized.")

        url = f"https://bid.cars/en/search/archived/results?search-type=typing&query={search_query}&status=All&make=All&model=All&year-from=1900&year-to=2026&auction-type=All"
        print(f"Opening URL: {url}")
        driver.get(url)
        time.sleep(5)

        print("Scraping data...")
        car_titles = driver.find_elements(By.CLASS_NAME, "item-title.damage-info")
        bid_prices = driver.find_elements(By.CLASS_NAME, "price-box")
        milage = driver.find_elements(By.CLASS_NAME, "odo_desc.no-wrap-text-ellipsis")
        damage = driver.find_elements(By.XPATH, '//li[@class="damage-info"]')

        for i in range(len(car_titles)):
            title = car_titles[i].text
            
            try:
                car_milage = milage[i].text.strip().split(':')[-1].strip()
                final_bid = bid_prices[i].text.strip().split(':')[-1].strip()
                car_damage = damage[i].text.strip().split(':')[-1].strip()
            except IndexError:
                car_milage = "no milage"
                final_bid = "No bid"
                car_damage = "No damage info"

            car = Car(title=title, final_bid=final_bid, car_milage=car_milage, car_damage=car_damage)
            db.session.add(car)

        db.session.commit()
        print("Data saved.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        driver.quit()
        print("WebDriver closed.")


@app.route('/')
def index():
    cars = Car.query.all()
    return render_template('table.html', cars=cars)

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        query = request.form['query']
        print(f"User entered query: {query}")
        success = scrape_bid_cars(query)

        if success:
            return redirect(url_for('index'))
        else:
            return "An error occurred during scraping."

    return render_template('scrape_form.html')

if __name__ == '__main__':
    app.run(debug=True)