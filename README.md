# Frame & Lens ETL Pipeline
## 📌 Project Overview
This project is a web scraping ETL pipeline built using Python to extract eyeglasses product data from:

https://www.glasses.com/gl-us/eyeglasses

The goal of this project was to practice real-world data extraction from a dynamic e-commerce website and structure the data for further analysis or storage.

Instead of scraping all available pages, a controlled for loop was implemented to limit the number of pages scraped. This approach was intentional to:

* Reduce unnecessary load on the website

* Improve scraping efficiency

* Control dataset size for analysis

## 🛠 Tech Stack

* Python

* Selenium (for handling dynamic content and infinite scroll)

* BeautifulSoup (for HTML parsing)

* Pandas (for data transformation and export)

* SQLAlchemy & PostgreSQL (prepared for database integration)

* dotenv (for environment variable management)

## ⚙️ How the Pipeline Works
### 1️⃣ Page Loading
Selenium WebDriver is used to open the website and render dynamic content.
### 2️⃣ Controlled Pagination
A for loop iterates through selected pages
### 3️⃣ Infinite Scroll Handling
The script scrolls to the bottom of each page until no new content loads.

### 4️⃣ Data Extraction
For each product tile, the following fields are extracted:

* Product Code

* Product Brand

* Price

### 5️⃣ Data Storage
Extracted data is stored in a Pandas DataFrame and exported as csv

### 📌 Key Learning Outcomes
* Handling dynamic websites with Selenium

* Managing infinite scroll behavior

* Structuring ETL workflows

* Preventing redundant scraping

* Exporting structured datasets for analysis


