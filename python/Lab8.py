import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.select("td.titleColumn a")
authors = soup.select("td.titleColumn span.secondaryInfo")
ratings = soup.select("td.ratingColumn strong")

for title, author, rating in zip(titles, authors, ratings):
    print(title.text.strip(), author.text.strip(), rating.text.strip())