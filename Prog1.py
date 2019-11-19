import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
soup=BeautifulSoup(page.content, 'html.parser')
containers=soup.find("tbody",{"class":"lister-list"})

items=(containers.findAll('tr'))
items1=(containers.findAll('a'))

filename = "Imdb_Movies.csv"
f=open(filename,"w")
headers = ("Links, Movie name\n")

f.write(headers)

for item in items:
    moviename=item.find(class_='titleColumn').get_text().strip().replace("\n", "").replace(",", "")
    #rating=item.find(class_='ratingColumn imdbRating').get_text().strip()
    link = "https://www.imdb.com/" + (item.td.a["href"])

    f.write(link + "," +moviename + "\n" )

f.close()
