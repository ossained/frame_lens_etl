# %% [markdown]
# ## Frame & Lens ETL pipeline

# %%
# import required libraries
# web scarping librabris
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# import manipulation libraries
import pandas as pd


# database libraries
from sqlalchemy import create_engine
import psycopg2

# evn
from dotenv import load_dotenv
import os 

import time

# %% [markdown]
# ## Loading the page

# %%
page_num = 1
url = "https://www.glasses.com/gl-us/eyeglasses"

# set up selenium webdriver
options = Options()
options.headless = False
service = Service(ChromeDriverManager().install())

# initialize the webdriver 
driver = webdriver.Chrome(service=service,options=options)

#load the webpage
driver.get(url)

#wait for the page to load 
time.sleep(20)


# %% [markdown]
# ## Handling infinite scroll

# %%


glasses_data = []

for page_num in range(1, 30):

    full_url = f"{url}?page={page_num}"
    print(f"Loading: {full_url}")

    driver.get(full_url)
    time.sleep(3)

    # Scroll
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print(f"Finished scrolling page {page_num}")

    # ✅ SCRAPE INSIDE LOOP
    soup = BeautifulSoup(driver.page_source, "html.parser")
    glasses = soup.find_all("a", class_="product-tile")

    print(f"Found {len(glasses)} products on page {page_num}")

    for glass in glasses:

        code_element = glass.find('div', class_='product-code')
        product_code = code_element.text.strip() if code_element else 'N/A'

        brand_element = glass.find('div', class_='product-brand')
        product_brand = brand_element.text.strip() if brand_element else 'N/A'

        price_element = glass.find(class_='product-price')
        price = price_element.get_text(strip=True) if price_element else 'N/A'

        glasses_data.append({
            'page': page_num,   # helpful for debugging
            'product_code': product_code,
            'product_brand': product_brand,
            'price': price
        })

print(f"Total products scraped: {len(glasses_data)}")
    
    

# %%
print(glasses_data)

# %%
glasses_df = pd.DataFrame(glasses_data)
print(glasses_df)

# %%


# %%
glasses_df.to_csv("glasses_data.csv", index=False)

# %%
print(glasses_df.shape)

# %%



