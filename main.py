import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
movies = soup.find_all(name='h3', class_='title')

movie_titles = [movie.text for movie in movies]

top_movies = movie_titles[::-1]

# print(top_movies[58])
with open("top_movies.txt", mode='w', encoding='utf-8') as file:
    for mov in top_movies:
        file.write(f'{mov}\n')
