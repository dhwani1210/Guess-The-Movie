import requests
from bs4 import BeautifulSoup
# import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies=[]

movie_table = soup.find_all("table", {"class": "wikitable plainrowheaders defaultcenter col2left"})

for i in movie_table:
    
    movie_list= i.find_all("th", {"scope": "row"})

    for tags in movie_list:
        a_tags = tags.find_all("a")
        for movie_title in a_tags:
            if "The Marvels" in movies:
                break
            movies.append(movie_title.text.strip())

# print(movies)