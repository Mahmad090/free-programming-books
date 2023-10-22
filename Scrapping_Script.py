# here is the script for Scrapping any book data from https://www.goodreads.com/ site 
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
fieldnames = ['title', 'author', 'description', 'genres', 'pages', 'rating']
result = requests.get(link)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box1 = soup.find('div', class_='BookPage__rightColumn')

    if box1 is not None:
        title = box1.find('h1', class_='Text Text__title1').get_text()
        box2 = soup.find('div', class_='BookPageMetadataSection')
        author = box2.find('span', class_='ContributorLink__name').get_text()
        rating = box2.find('div', class_='RatingStatistics__rating').get_text()
        des = box2.find('span', class_='Formatted').get_text()
        pages = soup.find('p', {'data-testid': 'pagesFormat'})
        if(pages):
            pages=pages.get_text()
        genres_container = soup.find('ul', {'aria-label': 'Top genres for this book'})
        genres = []

        if genres_container:
            genre_links = genres_container.find_all('span', class_='Button__labelItem')
            genres = [link.get_text() for link in genre_links]

        print("Book No:")
        genres = genres[:-1]
        genres = set(genres)

        data = [{'title': title, 'author': author, 'description': des, 'genres': genres, 'pages': pages, 'rating': rating}]
        with open("./booksChris.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows(data)
