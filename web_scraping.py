import requests
import pandas as pd
from bs4 import BeautifulSoup

# Website to scrape
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)

# Check whether the request was successful
if response.status_code == 200:
    print("Website accessed successfully!")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Store scraped data
    books_data = []

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # Book title
        title = book.h3.a["title"]

        # Book price
        price = book.find("p", class_="price_color").text.strip()

        # Book rating
        rating = book.find("p", class_="star-rating")["class"][1]

        # Availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    # Create DataFrame
    df = pd.DataFrame(books_data)

    # Save CSV inside data folder
    df.to_csv("data/scraped_books.csv", index=False)

    print("\nScraping completed successfully!")
    print(f"Total books scraped: {len(df)}")
    print("\nFirst 5 records:")
    print(df.head())

else:
    print("Failed to access the website.")
    print("Status code:", response.status_code)