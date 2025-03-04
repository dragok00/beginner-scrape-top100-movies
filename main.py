from bs4 import BeautifulSoup
import requests
import sys

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")


articles = soup.find_all(name = "h2")
article_movies = []

for article_tag in articles:
    article_movies.insert(0, article_tag.getText())
    
del article_movies[100]
    
with open("100-best-movies.txt", "w", encoding = "utf-8") as file:
    for article in article_movies:
        file.write(article + "\n")