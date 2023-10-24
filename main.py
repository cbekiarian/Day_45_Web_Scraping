import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")

titles = soup.find_all("h3", class_="title")
titles = [name.getText() for name in titles]
titles.reverse()
with open("movies.txt","a",encoding="utf-8") as file:
    for item in titles:
        file.write(f"{item}\n")

