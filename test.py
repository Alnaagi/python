# from twill.commands import *
# import requests
# go('http://10.51.0.5/')

# fv("1", "loginform-username", "admin")
# fv("1", "loginform-password", "iontel2019#")

# submit('0')


# url = 'http://10.51.0.5/'

# # Create a session to persist the authentication

# session = requests.Session()

# # Now access the data page
# response = session.get(url)

# # Check if the page is fetched correctly
# if response.status_code == 200:
#     print("Page fetched successfully!")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
# import requests
import pandas as pd
import csv

with  sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto('http://10.51.0.5/')
#     url = "http://10.51.0.5/"
#     session = requests.Session()
#     response = session.get(url)
# if response.status_code == 200:
#     print("Page fetched successfully!")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page.fill('input#loginform-username','admin')
    page.fill('input#loginform-password','iontel2019#')
    page.click('input[type=submit]')
    page.reload
    page.click('div[class=appGlobalSideNav__item]')
    page.locator('"Discovery"').click()
    
    # page.click('div[class=appSwitcher__itemText]')
    # page.goto('http://10.51.0.5/#dashboard/discovery.cgi')
    html = page.inner_html('div[class=tableRegion]')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("div",class_ = "dataTables_scroll")
    # print(table)
    headers = table.find_all("th", )
    titles = []
    for i in headers:
      title = i.text
      titles.append(title)
    df = pd.DataFrame(columns=titles)
    # max_size = 7
    # dflist = df.apply(lambda x: ' '.join(x.split(maxsplit=max_size)[:max_size]))
    # remove_list = [r'[^\w\s]', r'\b\w{1,3}\b',]

    # df['description'].replace('|'.join(remove_list), '', regex=True)
    df = list(dict.fromkeys(df))
    print (df)

    # print(df)
    rows = table.find_all("tr")
    # print(rows)
    for i in rows[2:]:
      data = i.find_all("td")
      # print(i.text)
      row = [tr.text for tr in data ]
      print(row)
      # l = len(df)
      # df.loc[l]= row
      # print(df)


    mac_address = soup.find_all('td', attrs={'class': 'macAddress'})
    hostname = soup.find('td', {'class': 'hostname'})
    wmode = soup.find('td', {'class': 'wmode'}).text
    essid = soup.find('td', {'class': 'essid'}).text
    product = soup.find('td', {'class': 'product'}).text
    fwversion = soup.find('td', {'class': 'fwversion'}).text
    ipAddress = soup.find('td', {'class': 'ipAddress'}).text
    # print(f'mac address = {mac_address}')
    # print(mac_address)
    # print(f'hostname = {hostname.text}')
    # print(f'wmode = {wmode}')
    # print(f'essid = {essid}')
    # print(f'product = {product}')
    # print(f'fwversion = {fwversion}')
    # print(f'ipAddress = {ipAddress}')
    # print(headers)
    page = browser.new_page()
    page.goto('http://10.51.0.6/')
#     url = "http://10.51.0.5/"
#     session = requests.Session()
#     response = session.get(url)
# if response.status_code == 200:
#     print("Page fetched successfully!")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page.fill('input#loginform-username','admin')
    page.fill('input#loginform-password','iontel2019#')
    page.click('input[type=submit]')
    page.reload
    page.click('div[class=appGlobalSideNav__item]')
    page.locator('"Discovery"').click()
    
    # page.click('div[class=appSwitcher__itemText]')
    # page.goto('http://10.51.0.5/#dashboard/discovery.cgi')
    html = page.inner_html('div[class=tableRegion]')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("div",class_ = "dataTables_scroll")
    # print(table)
    headers = table.find_all("th", )
    titles = []
    for i in headers:
      title = i.text
      titles.append(title)
    df = pd.DataFrame(columns=titles)
    # max_size = 7
    # dflist = df.apply(lambda x: ' '.join(x.split(maxsplit=max_size)[:max_size]))
    # remove_list = [r'[^\w\s]', r'\b\w{1,3}\b',]

    # df['description'].replace('|'.join(remove_list), '', regex=True)
    df = list(dict.fromkeys(df))
    print (df)

    # print(df)
    rows = table.find_all("tr")
    # print(rows)
    for i in rows[2:]:
      data = i.find_all("td")
      # print(i.text)
      row = [tr.text for tr in data ]
      print(row)
      # l = len(df)
      # df.loc[l]= row
      # print(df)


    mac_address = soup.find_all('td', attrs={'class': 'macAddress'})
    hostname = soup.find('td', {'class': 'hostname'})
    wmode = soup.find('td', {'class': 'wmode'}).text
    essid = soup.find('td', {'class': 'essid'}).text
    product = soup.find('td', {'class': 'product'}).text
    fwversion = soup.find('td', {'class': 'fwversion'}).text
    ipAddress = soup.find('td', {'class': 'ipAddress'}).text
    # print(f'mac address = {mac_address}')
    # print(mac_address)
    # print(f'hostname = {hostname.text}')
    # print(f'wmode = {wmode}')
    # print(f'essid = {essid}')
    # print(f'product = {product}')
    # print(f'fwversion = {fwversion}')
    # print(f'ipAddress = {ipAddress}')
    # print(headers)    
    
# with open("ion.csv", mode="w") as csvfile:
#     fieldnames = df
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(row)
    page = browser.new_page()
    page.goto('http://10.51.0.7/')
#     url = "http://10.51.0.5/"
#     session = requests.Session()
#     response = session.get(url)
# if response.status_code == 200:
#     print("Page fetched successfully!")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page.fill('input#loginform-username','admin')
    page.fill('input#loginform-password','iontel2019#')
    page.click('input[type=submit]')
    page.reload
    page.click('div[class=appGlobalSideNav__item]')
    page.locator('"Discovery"').click()
    
    # page.click('div[class=appSwitcher__itemText]')
    # page.goto('http://10.51.0.5/#dashboard/discovery.cgi')
    html = page.inner_html('div[class=tableRegion]')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("div",class_ = "dataTables_scroll")
    # print(table)
    headers = table.find_all("th", )
    titles = []
    for i in headers:
      title = i.text
      titles.append(title)
    df = pd.DataFrame(columns=titles)
    # max_size = 7
    # dflist = df.apply(lambda x: ' '.join(x.split(maxsplit=max_size)[:max_size]))
    # remove_list = [r'[^\w\s]', r'\b\w{1,3}\b',]

    # df['description'].replace('|'.join(remove_list), '', regex=True)
    df = list(dict.fromkeys(df))
    print (df)

    # print(df)
    rows = table.find_all("tr")
    # print(rows)
    for i in rows[2:]:
      data = i.find_all("td")
      # print(i.text)
      row = [tr.text for tr in data ]
      print(row)
      # l = len(df)
      # df.loc[l]= row
      # print(df)


    mac_address = soup.find_all('td', attrs={'class': 'macAddress'})
    hostname = soup.find('td', {'class': 'hostname'})
    wmode = soup.find('td', {'class': 'wmode'}).text
    essid = soup.find('td', {'class': 'essid'}).text
    product = soup.find('td', {'class': 'product'}).text
    fwversion = soup.find('td', {'class': 'fwversion'}).text
    ipAddress = soup.find('td', {'class': 'ipAddress'}).text
    # print(f'mac address = {mac_address}')
    # print(mac_address)
    # print(f'hostname = {hostname.text}')
    # print(f'wmode = {wmode}')
    # print(f'essid = {essid}')
    # print(f'product = {product}')
    # print(f'fwversion = {fwversion}')
    # print(f'ipAddress = {ipAddress}')
    # print(headers)

    page = browser.new_page()
    page.goto('http://10.51.0.8/')
#     url = "http://10.51.0.5/"
#     session = requests.Session()
#     response = session.get(url)
# if response.status_code == 200:
#     print("Page fetched successfully!")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
    page.fill('input#loginform-username','admin')
    page.fill('input#loginform-password','iontel2019#')
    page.click('input[type=submit]')
    page.reload
    page.click('div[class=appGlobalSideNav__item]')
    page.locator('"Discovery"').click()
    
    # page.click('div[class=appSwitcher__itemText]')
    # page.goto('http://10.51.0.5/#dashboard/discovery.cgi')
    html = page.inner_html('div[class=tableRegion]')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("div",class_ = "dataTables_scroll")
    # print(table)
    headers = table.find_all("th", )
    titles = []
    for i in headers:
      title = i.text
      titles.append(title)
    df = pd.DataFrame(columns=titles)
    # max_size = 7
    # dflist = df.apply(lambda x: ' '.join(x.split(maxsplit=max_size)[:max_size]))
    # remove_list = [r'[^\w\s]', r'\b\w{1,3}\b',]

    # df['description'].replace('|'.join(remove_list), '', regex=True)
    df = list(dict.fromkeys(df))
    print (df)

    # print(df)
    rows = table.find_all("tr")
    # print(rows)
    for i in rows[2:]:
      data = i.find_all("td")
      # print(i.text)
      row = [tr.text for tr in data ]
      print(row)
      # l = len(df)
      # df.loc[l]= row
      # print(df)


    mac_address = soup.find_all('td', attrs={'class': 'macAddress'})
    hostname = soup.find('td', {'class': 'hostname'})
    wmode = soup.find('td', {'class': 'wmode'}).text
    essid = soup.find('td', {'class': 'essid'}).text
    product = soup.find('td', {'class': 'product'}).text
    fwversion = soup.find('td', {'class': 'fwversion'}).text
    ipAddress = soup.find('td', {'class': 'ipAddress'}).text
    # print(f'mac address = {mac_address}')
    # print(mac_address)
    # print(f'hostname = {hostname.text}')
    # print(f'wmode = {wmode}')
    # print(f'essid = {essid}')
    # print(f'product = {product}')
    # print(f'fwversion = {fwversion}')
    # print(f'ipAddress = {ipAddress}')
    # print(headers)