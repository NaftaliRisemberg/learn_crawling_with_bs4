import requests
from bs4 import BeautifulSoup

# Fetch the content of the webpage
url = "https://www.ynet.co.il/news/category/184"
response = requests.get(url)


song_soup = BeautifulSoup(response.text, "html.parser")

#print(type(song_soup))

# show the html page in nice order
#print(song_soup.prettify())

# show the title page in text
# the string show only the text
title_text = song_soup.title.string

#div = song_soup.div

# if i wanna get the title with the id 'zep' i can use
#song_soup.find(id='zep')

# get only the text
#s = song_soup.find(id='zep').get_text()

# get the all divs with the id
#hls = song_soup.find_all("h1")
# or
#print(song_soup("li"))

