import requests
from bs4 import BeautifulSoup
import csv

URL = "http://books.toscrape.com/"

def scrape_books():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        data.append({"Title": title, "Price": price, "Availability": availability})

    return data

def save_to_csv(data, filename="scraped_books.csv"):
    if not data:
        print("No data to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Availability"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} items to {filename}")

def main():
    print("Scraping book data...")
    books = scrape_books()

    if books:
        for book in books:
            print(f"{book['Title']} - {book['Price']} - {book['Availability']}")
        save_to_csv(books)
    else:
        print("No books were scraped.")

if __name__ == "__main__":
    main()