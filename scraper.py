import requests
from bs4 import BeautifulSoup
import pandas as pd

URLS = [
    "https://store.steampowered.com/app/730/CounterStrike_2/",
    "https://store.steampowered.com/app/570/Dota_2/",
    "https://store.steampowered.com/app/1091500/Cyberpunk_2077/"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

games = []

for url in URLS:
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed: {url}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("div", class_="apphub_AppName")

    price = soup.find("div", class_="game_purchase_price price")

    discount = soup.find("div", class_="discount_pct")

    games.append({
        "title": title.text.strip() if title else "N/A",
        "price": price.text.strip() if price else "Free / N/A",
        "discount": discount.text.strip() if discount else "No discount"
    })

df = pd.DataFrame(games)

df.to_csv("steam_games.csv", index=False)

print(df)
print("\nSaved to steam_games.csv")
