import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

a = float(input("Rating filtresi gir (örn. 8.5): "))

# Her bir film kutusu burada bir <li> etiketi içinde
film_kutulari = soup.find_all("li", class_="ipc-metadata-list-summary-item")

for kutu in film_kutulari:
    # Film ismini bul
    baslik_tag = kutu.find("a", class_="ipc-title-link-wrapper")
    if not baslik_tag:
        continue
    baslik = baslik_tag.text.strip()

    # Rating değerini bul
    rating_tag = kutu.find("span", class_="ipc-rating-star--imdb")
    if not rating_tag:
        continue
    rating_text = rating_tag.text.strip().replace("IMDb", "")[:3]

    try:
        rating = float(rating_text)
    except ValueError:
        continue

    if rating > a:
        print(f"🎬 Film: {baslik} | ⭐ IMDB Rating: {rating}")
