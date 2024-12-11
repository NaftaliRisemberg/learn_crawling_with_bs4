import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.ynet.co.il/news/category/184"
response = requests.get(url)

news_soup = BeautifulSoup(response.content, "html.parser")

mtag = news_soup.findAll("div", attrs={"class": "title"})
texts = [tag.get_text() for tag in mtag]


def insert_data(data):
    # פותחים את הקובץ רק פעם אחת
    with open('news.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for text in data:
            writer.writerow([text, 1])
    return "Data inserted successfully"

print(texts)
insert_data(texts)


