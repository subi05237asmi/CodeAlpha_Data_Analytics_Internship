# CodeAlpha Task 1 - Web Scraping

## 🕷️ Web Scraping Project

This project was completed as part of my **CodeAlpha Data Analytics Internship**.

The objective of this task was to use Python and web scraping techniques to extract useful information from a website, process the collected data, and save it as a structured dataset.

---

## 🎯 Objective

The main objectives of this project are:

- Extract data from a publicly available website.
- Understand the basic structure of HTML pages.
- Use Python libraries for web scraping.
- Extract relevant information from HTML elements.
- Store the collected information in a structured format.
- Export the scraped data into a CSV file.

---

## 🌐 Website Used

**Books to Scrape**

Website:

https://books.toscrape.com/

Books to Scrape is a website designed for practicing web scraping techniques.

---

## 🛠️ Technologies & Libraries Used

- **Python**
- **Requests**
- **BeautifulSoup**
- **Pandas**
- **HTML**
- **CSV**

---

## 📌 Data Collected

The scraper collects the following information for each book:

| Column | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Rating | Book rating |
| Availability | Availability status |

---

## ⚙️ How the Project Works

The project follows these steps:

```text
Website
   ↓
Send HTTP Request
   ↓
Receive HTML Response
   ↓
Parse HTML using BeautifulSoup
   ↓
Extract Book Information
   ↓
Create Pandas DataFrame
   ↓
Save Data as CSV