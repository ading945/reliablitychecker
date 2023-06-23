import requests
from bs4 import BeautifulSoup
from pycite.pycite import PyCite
import json
import os
from datetime import datetime


class UrlInfo:

    def __init__(self, url):
        self.url = url 
        self.publication_date = str(self.find_publication_date())
        

    def find_publication_date(self):
 
        #takes URL
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        #finds meta data for publication date
        publication_date = soup.find('meta', attrs={'property': 'article:published_time'})
        
        if publication_date:
            return publication_date['content']
        else:
            return None
    '''    
    def find_publication_date(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        publication_date = soup.find('time', class_='publication-date')

        if publication_date:
            return publication_date.text
        else:
            return None
    '''
    def calculate_score(self):

        current_date = datetime.now()
        #converts object to string representation
        published_datetime = datetime.strptime(self.publication_date, "%Y-%m-%dT%H:%M:%SZ")
        time_difference = current_date - published_datetime
        #converts to day format
        days_difference = time_difference.days
       
        # Calculate variable value based on proximity of published date to current date
        if days_difference <= 365:
            reliability_score = 10
        elif days_difference <= 730:
            reliability_score = 8
        elif days_difference <= 1460:
            reliability_score = 5
        elif days_difference <= 3000:
            reliability_score = 3
        else:
            reliability_score = 1

        return reliability_score

    def find_publisher(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        #scrapes for publisher
        publisher = soup.find('meta', attrs={'property': 'og:site_name'})
        
        if publisher:
            return publisher['content']
        else:
            return None
    #Doesnt seem to work    
    def find_author(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

   

        #If the author is inside a <meta> tag with the property "author"
        author = soup.find('meta', attrs={'property': 'author'})

        if author:
            return author['content']
        else:
            return None
    def scrape_article_content(self):

        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Add code specific to the website's HTML structure to scrape the article content.
        # This will vary depending on the website you're scraping.

        # Example: If the article content is inside <div> elements with a specific class
        article_content = soup.find_all('div', class_='article-content')

        if article_content:
            # Combine the contents of multiple elements if needed
            article_text = ' '.join([element.get_text() for element in article_content])
            return article_text
        else:
            return None
