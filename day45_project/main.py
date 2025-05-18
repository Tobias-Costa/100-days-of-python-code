import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def save_file(movie):
    with open("movies.txt", "a", encoding="utf-8") as file:
            file.write(f"{movie}\n")

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
movies_list = [ movie.getText() for movie in soup.find_all(name="h3", class_="title") ]

for movie in reversed(movies_list):
    save_file(movie)