
import time
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path


# ======================================================
# PATHS (raíz del proyecto, independiente del lugar run)
# ======================================================
# Este archivo vive en:
# books-pipeline/src/extract/scrape_all_pages.py
# parents[2] sube: extract -> src -> books-pipeline
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Salida del CSV:
# books-pipeline/data/raw/books_raw.csv
OUT_PATH = PROJECT_ROOT / "data" / "raw" / "books_raw.csv"

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


# ======================
# SCRAPE UNA PÁGINA
# ======================
def scrape_page(page_num: int) -> list[dict]:
    url = BASE_URL.format(page_num)
    html = requests.get(url, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("article.product_pod")
    if not cards:
        return []

    books = []

    for card in cards:
        title = card.select_one("h3 a").get("title")

        price = card.select_one("p.price_color").get_text(strip=True)
        price = price.replace("Â", "").replace("£", "")

        rating_tag = card.select_one("p.star-rating")
        classes = rating_tag.get("class", [])
        rating = next((c for c in classes if c != "star-rating"), None)

        href = card.select_one("h3 a").get("href")
        link = urljoin(url, href)

        books.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "url": link,
            "page_num": page_num
        })

    return books


# ======================
# SCRAPE TODAS LAS PÁGINAS
# ======================
def scrape_all(max_pages: int = 60) -> list[dict]:
    all_books = []

    for page in range(1, max_pages + 1):
        data = scrape_page(page)

        if not data:
            print(f"Stopped at page {page} (no books found).")
            break

        all_books.extend(data)
        print(f"Page {page}: {len(data)} books | Total: {len(all_books)}")
        time.sleep(0.5)

    return all_books


# ======================
# GUARDAR CSV (ROBUSTO)
# ======================
def save_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        return

    # Crear data/raw si no existe
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# ======================
# MAIN
# ======================
if __name__ == "__main__":
    books = scrape_all()
    save_csv(books, OUT_PATH)
    print(f"Saved: {len(books)} rows to {OUT_PATH}")
