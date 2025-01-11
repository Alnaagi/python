# # # # from playwright.sync_api import sync_playwright
# # # # from bs4 import BeautifulSoup
# # # # import pandas as pd
# # # # import csv

# # # # with  sync_playwright() as p:
# # # #     browser = p.chromium.launch(headless=False, slow_mo=3000)
# # # #     page = browser.new_page()
# # # #     page.goto('http://10.51.0.5/')
# # # #     page.fill('input#loginform-username','admin')
# # # #     page.fill('input#loginform-password','iontel2019#')
# # # #     page.click('input[type=submit]')
# # # #     page.reload
# # # #     page.click('div[class=appGlobalSideNav__item]')
# # # #     page.locator('"Discovery"').click()
    
# # # #     html = page.inner_html('div[class=tableRegion]')
  
# # # #     soup = BeautifulSoup(html, 'lxml')
# # # #     table = soup.find("div",class_ = "dataTables_scroll")
   
# # # #     headers = table.find_all("th", )
# # # #     titles = []
# # # #     for i in headers:
# # # #       title = i.text
# # # #       titles.append(title)
# # # #     df = pd.DataFrame(columns=titles)
# # # #     df = list(dict.fromkeys(df))
# # # #     print (df)

   
# # # #     rows = table.find_all("tr")
  
# # # #     for i in rows[2:]:
# # # #       data = i.find_all("td")
# # # #       row = [tr.text for tr in data ]
# # # #       print(row)


# # # #     mac_address = soup.find_all('td', attrs={'class': 'macAddress'})
# # # #     hostname = soup.find('td', {'class': 'hostname'})
# # # #     wmode = soup.find('td', {'class': 'wmode'}).text
# # # #     essid = soup.find('td', {'class': 'essid'}).text
# # # #     product = soup.find('td', {'class': 'product'}).text
# # # #     fwversion = soup.find('td', {'class': 'fwversion'}).text
# # # #     ipAddress = soup.find('td', {'class': 'ipAddress'}).text


# # # from playwright.sync_api import sync_playwright
# # # from bs4 import BeautifulSoup
# # # import sqlite3
# # # import pandas as pd

# # # # Database setup
# # # def init_db():
# # #     conn = sqlite3.connect("data.db")
# # #     cursor = conn.cursor()
# # #     cursor.execute("""
# # #         CREATE TABLE IF NOT EXISTS discovery_data (
# # #             mac_address TEXT,
# # #             hostname TEXT,
# # #             wmode TEXT,
# # #             essid TEXT,
# # #             product TEXT,
# # #             fwversion TEXT,
# # #             ip_address TEXT
# # #         )
# # #     """)
# # #     conn.commit()
# # #     conn.close()

# # # def save_to_db(data):
# # #     conn = sqlite3.connect("data.db")
# # #     cursor = conn.cursor()
# # #     cursor.executemany("""
# # #         INSERT INTO discovery_data (mac_address, hostname, wmode, essid, product, fwversion, ip_address)
# # #         VALUES (?, ?, ?, ?, ?, ?, ?)
# # #     """, data)
# # #     conn.commit()
# # #     conn.close()

# # # def scrape_data():
# # #     with sync_playwright() as p:
# # #         browser = p.chromium.launch(headless=True)
# # #         page = browser.new_page()

# # #         # Login
# # #         page.goto('http://10.51.0.5/')
# # #         page.fill('input#loginform-username', 'admin')
# # #         page.fill('input#loginform-password', 'iontel2019#')
# # #         page.click('input[type=submit]')
# # #         page.click('div[class=appGlobalSideNav__item]')
# # #         page.locator('"Discovery"').click()

# # #         # Scrape table data
# # #         html = page.inner_html('div[class=tableRegion]')
# # #         soup = BeautifulSoup(html, 'lxml')
# # #         table = soup.find("div", class_="dataTables_scroll")
        
# # #         # Extract rows
# # #         rows = table.find_all("tr")[2:]
# # #         data = []
# # #         for row in rows:
# # #             cells = row.find_all("td")
# # #             if len(cells) >= 7:
# # #                 mac_address = cells[0].text.strip()
# # #                 hostname = cells[1].text.strip()
# # #                 wmode = cells[2].text.strip()
# # #                 essid = cells[3].text.strip()
# # #                 product = cells[4].text.strip()
# # #                 fwversion = cells[5].text.strip()
# # #                 ip_address = cells[6].text.strip()
# # #                 data.append((mac_address, hostname, wmode, essid, product, fwversion, ip_address))

# # #         browser.close()
# # #         return data

# # # if __name__ == "__main__":
# # #     init_db()
# # #     scraped_data = scrape_data()
# # #     save_to_db(scraped_data)
# # #     print("Data scraped and saved to database successfully!")

# # from playwright.sync_api import sync_playwright
# # from bs4 import BeautifulSoup
# # import sqlite3

# # # Database setup
# # def init_db():
# #     conn = sqlite3.connect("data.db")
# #     cursor = conn.cursor()
# #     cursor.execute("""
# #         CREATE TABLE IF NOT EXISTS discovery_data (
# #             mac_address TEXT,
# #             hostname TEXT,
# #             wmode TEXT,
# #             essid TEXT,
# #             product TEXT,
# #             fwversion TEXT,
# #             ip_address TEXT
# #         )
# #     """)
# #     conn.commit()
# #     conn.close()

# # def save_to_db(data):
# #     conn = sqlite3.connect("data.db")
# #     cursor = conn.cursor()
# #     cursor.executemany("""
# #         INSERT INTO discovery_data (mac_address, hostname, wmode, essid, product, fwversion, ip_address)
# #         VALUES (?, ?, ?, ?, ?, ?, ?)
# #     """, data)
# #     conn.commit()
# #     conn.close()

# # # Scraping function
# # def scrape_data():
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=False, slow_mo= 3000)
# #         page = browser.new_page()

# #         # Login
# #         page.goto('http://10.51.0.5/')
# #         page.fill('input#loginform-username', 'admin')
# #         page.fill('input#loginform-password', 'iontel2019#')
# #         page.click('input[type=submit]')
# #         page.click('div[class=appGlobalSideNav__item]')
# #         page.locator('"Discovery"').click()

# #         # Scrape table data
# #         html = page.inner_html('div[class=tableRegion]')
# #         soup = BeautifulSoup(html, 'lxml')
# #         table = soup.find("div", class_="dataTables_scroll")
        
# #         # Extract rows
# #         rows = table.find_all("tr")[2:]
# #         data = []
# #         for row in rows:
# #             cells = row.find_all("td")
# #             if len(cells) >= 7:
# #                 mac_address = cells[0].text.strip()
# #                 hostname = cells[1].text.strip()
# #                 wmode = cells[2].text.strip()
# #                 essid = cells[3].text.strip()
# #                 product = cells[4].text.strip()
# #                 fwversion = cells[5].text.strip()
# #                 ip_address = cells[6].text.strip()
# #                 data.append((mac_address, hostname, wmode, essid, product, fwversion, ip_address))

# #         browser.close()
# #         return data

# # # Main function
# # if __name__ == "__main__":
# #     init_db()
# #     scraped_data = scrape_data()
# #     save_to_db(scraped_data)
# #     print("Data scraped and saved to database successfully!")


# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup
# import sqlite3

# # List of IPs to scrape
# IP_ADDRESSES = [
#     "http://10.51.0.5/",
#     "http://10.51.0.6/",
#     "http://10.51.0.7/",
#     "http://10.51.0.8/",
# ]

# # Function to save data to SQLite
# def save_to_db(data):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS discovery_data (
#             mac_address TEXT,
#             hostname TEXT,
#             wmode TEXT,
#             essid TEXT,
#             product TEXT,
#             fwversion TEXT,
#             ip_address TEXT
#         )
#     """)
#     cursor.executemany("""
#         INSERT INTO discovery_data (
#             mac_address, hostname, wmode, essid, product, fwversion, ip_address
#         ) VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, data)
#     conn.commit()
#     conn.close()

# # Function to scrape a single IP
# def scrape_ip(ip_address, playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=3000)
#     page = browser.new_page()
    
#     page.goto(ip_address)
#     page.fill("input#loginform-username", "admin")
#     page.fill("input#loginform-password", "iontel2019#")
#     page.click("input[type=submit]")
#     page.reload()
#     page.click("div[class=appGlobalSideNav__item]")
#     page.locator('"Discovery"').click()
    
#     html = page.inner_html("div[class=tableRegion]")
#     browser.close()
    
#     soup = BeautifulSoup(html, "lxml")
#     table = soup.find("div", class_="dataTables_scroll")
#     rows = table.find_all("tr")
    
#     scraped_data = []
#     for i in rows[2:]:  # Skip header rows
#         data = i.find_all("td")
#         row = [td.text.strip() for td in data]
#         if len(row) == 6:  # Ensure the row has enough data
#             row.append(ip_address)  # Add the IP address to each row
#             scraped_data.append(row)
    
#     return scraped_data

# # Main function
# def main():
#     all_data = []
#     with sync_playwright() as playwright:
#         for ip in IP_ADDRESSES:
#             try:
#                 print(f"Scraping data from {ip}...")
#                 data = scrape_ip(ip, playwright)
#                 all_data.extend(data)
#             except Exception as e:
#                 print(f"Error scraping {ip}: {e}")
    
#     print(f"Scraped data: {len(all_data)} records.")
#     save_to_db(all_data)
#     print("Data saved to database.")

# if __name__ == "__main__":
#     main()
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import sqlite3

IP_ADDRESSES = [
    "http://10.51.0.5/",
    "http://10.51.0.6/",
    "http://10.51.0.7/",
    "http://10.51.0.8/",
]

def save_to_db(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Drop the table if it exists to recreate with the correct schema
    cursor.execute("DROP TABLE IF EXISTS discovery_data")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS discovery_data (
            mac_address TEXT,
            hostname TEXT,
            wmode TEXT,
            essid TEXT,
            product TEXT,
            fwversion TEXT,
            ip_address TEXT,
            source_url TEXT
        )
    """)
    if data:
        print(f"Data to insert: {data}")  # Debug data being saved
        cursor.executemany("""
            INSERT INTO discovery_data (
                mac_address, hostname, wmode, essid, product, fwversion, ip_address, source_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        print(f"Inserted {len(data)} rows into the database.")
    else:
        print("No data to insert.")
    conn.commit()
    conn.close()



def scrape_ip(ip_address, playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=3500)
    page = browser.new_page()
    page.goto(ip_address)
    page.fill("input#loginform-username", "admin")
    page.fill("input#loginform-password", "iontel2019#")
    page.click("input[type=submit]")
    page.reload()
    page.click("div[class=appGlobalSideNav__item]")
    page.locator('"Discovery"').click()

    html = page.inner_html("div[class=tableRegion]")
    browser.close()

    print(f"HTML content from {ip_address}: {html[:500]}")  # Debug HTML content

    soup = BeautifulSoup(html, "lxml")
    table = soup.find("div", class_="dataTables_scroll")
    if not table:
        print(f"No table found on {ip_address}")
        return []

    rows = table.find_all("tr")
    print(f"Found {len(rows)} rows in the table on {ip_address}")

    scraped_data = []
    for i in rows[2:]:
        data = i.find_all("td")
        row = [td.text.strip() for td in data]
        if len(row) < 6:  # Ensure row has enough columns
            print(f"Skipping incomplete row: {row}")
            continue
        row.append(ip_address)  # Add IP address
        scraped_data.append(row)
        print(f"Row data: {row}")  # Debug row data
    return scraped_data

def main():
    all_data = []
    with sync_playwright() as playwright:
        for ip in IP_ADDRESSES:
            try:
                print(f"Scraping data from {ip}...")
                data = scrape_ip(ip, playwright)
                all_data.extend(data)
            except Exception as e:
                print(f"Error scraping {ip}: {e}")
    
    print(f"Total scraped data: {len(all_data)} rows.")
    save_to_db(all_data)
    print("Data saved to database.")

if __name__ == "__main__":
    main()
