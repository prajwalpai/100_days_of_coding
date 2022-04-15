from bs4 import BeautifulSoup
import requests
import re
import random
from color import Color

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

all_tags = soup.find_all('h3')

movie_dict = {}
for item in all_tags:
    #rank,movie =
    movie = re.split('\)',item.getText())
    if '12' not in movie[0]:
        movie_dict[int(movie[0])] = movie[1]

for k,v in sorted(movie_dict.items()):
    print(k,v)

choice = 'y'

while choice == 'y':
    random_choice = random.randint(1, 100)
    print(Color.CYAN+Color.BOLD+f"\nHere is the movie recommendation of the day \nRank: {random_choice} :{movie_dict[random_choice]}"+Color.END)
    choice = input("Have you seen this movie? (y/n)")

print(Color.GREEN+f"\nGreat choice for today! Enjoy your movie{movie_dict[random_choice]}.\n"+Color.END)