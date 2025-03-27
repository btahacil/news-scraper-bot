# 📰 News Scraper Bot

This is a Python-based web scraping bot that automatically fetches the **latest news headlines** from [CNN Türk](https://www.cnnturk.com/) and saves them into a `.csv` file.

> ✅ Ideal for beginner data projects, freelance scraping tasks, and automation enthusiasts.

---

## 📌 Features

- 🔍 Scrapes real-time headlines from the homepage
- 📦 Saves data in CSV format with UTF-8 encoding
- ✅ Clean and lightweight codebase using `requests` and `BeautifulSoup4`

---

## 🧠 Technologies Used

- `Python 3.x`
- `requests`
- `beautifulsoup4`
- `csv`

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/btahacil/news-scraper-bot.git
   cd news-scraper-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Output will be saved in:
   ```
   haber_basliklari.csv
   ```

---

## 📷 Sample Output

```
News Scraper Bot Başladı...
-- Güncel Başlıklar --
- SON DAKİKA
- EKONOMİ
- TEKNOLOJİ
- SPOR
- MAGAZİN
...
```

---

## 📁 File Structure

```
├── main.py               # Main scraping script
├── requirements.txt      # Dependencies
└── README.md             # Project description
```

---

## 🙋‍♂️ Author

**Bünyamin Taha Çil**  
> Python Developer • Web Scraping Enthusiast • Automation Explorer  
📍 Ankara, Turkey  
🌐 GitHub: [@btahacil](https://github.com/btahacil)

---

## 🧩 Notes

This bot can easily be extended to:
- Pull headlines from multiple news sources
- Schedule scraping with `cron` or `task scheduler`
- Export data to Excel, PDF, or Google Sheets

