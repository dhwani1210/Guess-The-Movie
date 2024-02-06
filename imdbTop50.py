import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls033806763/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = []

for movie in soup.select("div.lister-item-content"):
    title_tag = movie.find("h3", class_="lister-item-header").find("a")
    if title_tag:
        title = title_tag.text.strip()
        movies.append(title)


# print(movies)