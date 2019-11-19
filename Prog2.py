import requests
from bs4 import BeautifulSoup
import json
import csv

with open("Imdb_Movies.csv") as infile:
    reader = csv.DictReader(infile)
    file = open("Finale1.json", "w")
    
    for link in reader:
        res = requests.get(link['Links'])
        soup = BeautifulSoup(res.content, 'html.parser')
        containers = soup.find(id="main_top")
        containers1 = soup.find(id="titleDetails")
        containers2 = soup.find("div", {"class": "poster"})
        containers3 = soup.find("div", {"class": "ratingValue"})
        items = (containers.findAll("div", {"class": 'credit_summary_item'}))


        name = containers.h1.get_text()
        #print("Movie Name: " + name)

        rate = containers3.span.text.strip()
        #print("Rating: " + rate)

        director = items[0].a.get_text()
        #print("Director: " + director)

        b_tags = items[1].findAll('a')
        writer = ' '.join(b.get_text(strip=True) for b in b_tags[:2])
        #print("Writer: " + writer)

        stars = items[2].findAll('a')
        star = ' '.join(star.get_text(strip=True) for star in stars[:-1])
        #print("Stars: " + star)

        item1s = (containers1.findAll("div", {"class": 'txt-block'}))


        release = item1s[3].contents[2].strip()
        #print("Realese Date: " + release)

        poster_url = containers2.img["src"]
        #print("Url: " + poster_url)

        output = {"Movie Name": name,
                  "Director": director,
                  "Writer": writer,
                  "Stars": star,
                  "Realease Date": release, "url": poster_url}

        json.dump(output, file, indent=4)


    file.close()

