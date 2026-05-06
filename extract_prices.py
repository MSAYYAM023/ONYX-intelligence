import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("book_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])
        print(f"{title} — {price}")

print("\nCSV file 'book_prices.csv' created.")