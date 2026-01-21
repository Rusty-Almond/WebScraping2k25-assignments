import requests
import bs4
from fake_useragent import UserAgent
import pandas as pd
import re
ua=UserAgent()
# user_agent=ua.random
#print(user_agent)
url_movies="https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}
response=requests.get(url_movies,headers=headers)
soup=bs4.BeautifulSoup(response.text,'html.parser')
print(soup.title)
title=soup.select('h3.ipc-title__text')
movies = [t.get_text(strip=True) for t in title[:25]]
print(len(movies))
print(movies)
movie_links=[]
k=0
for a in soup.find_all("a", href=True):
    href = a["href"]
    k=k+1
    if(k%2!=0):  # this is because the links are repeating so 2 times the links were entered
        if href.startswith("/title/tt"):
            movie_links.append("https://www.imdb.com" + href.split("?")[0])
print(len(movie_links))
print(movie_links)
data=[]
for i in range(25):
    response=requests.get(movie_links[i],headers=headers)
    soup=bs4.BeautifulSoup(response.text,'html.parser')
    rating=soup.select_one('div[data-testid="hero-rating-bar__aggregate-rating__score"]')
    rating_txt=rating.get_text(strip=True)
    plot = soup.select_one('span[data-testid="plot-xs_to_m"]')
    plot_txt = plot.get_text(strip=True)
    director=soup.select_one('li[data-testid="title-pc-principal-credit"] a')
    director_txt=director.get_text(strip=True)
    cast = soup.select('a[data-testid="title-cast-item__actor"]')[:5]
    cast_names = [c.get_text(strip=True) for c in cast]
    title_tag = soup.title.string
    year_match = re.search(r"\((\d{4})\)", title_tag)
    year = year_match.group(1)
    runtime_tag = soup.select_one('li[data-testid="title-techspec_runtime"] div:last-child')
    runtime = runtime_tag.get_text(strip=True)
    poster = soup.select_one('div[data-testid="hero-media__poster"]')
    poster_img=poster.find("img")
    poster_url = poster_img.get("src")
    cards = soup.select('div[data-testid="user-reviews-summary-featured-review-card"]')[:3]
    comments = []
    for card in cards:
        com = card.select_one('div[role="presentation"]')
        if com:
            comments.append(com.get_text(strip=True))
    data.append({
        "title":movies[i],
        "url":movie_links[i],
        "rating":rating,
        "plot":plot_txt,
        "rating":rating_txt,
        "director":director_txt,
        "cast":cast_names,
        "release_year":year,
        "duration":runtime,
        "image_url":poster_url,
        "comments":comments
    })
df=pd.DataFrame(data)
df.to_json("movies.json", orient="records", indent=4)
print(data)
