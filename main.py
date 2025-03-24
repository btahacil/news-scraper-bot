import requests
from bs4 import BeautifulSoup

print("News Scraper Bot Başladı...")

url = "https://www.cnnturk.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

headlines = soup.find_all("h2")  # Genellikle başlıklar h2 etiketiyle olur

print("\n--- Güncel Başlıklar ---\n")
for h in headlines:
    text = h.get_text(strip=True)
    if text:
        print("- " + text)

