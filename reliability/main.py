import requests
from bs4 import BeautifulSoup
from pycite.pycite import PyCite
import json
import os
from urlsort import UrlInfo


def main():
   
  x = UrlInfo("https://www.cnn.com/2023/06/20/weather/tropical-storm-bret-hurricane-tuesday/index.html")
  print(x.find_publisher())
  x.scrape_article_content()
  '''
  if x:
    # Store the content in a text file
    filename = 'article_content.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(x)
    print("Article content saved to", filename)
  else:
      print("Article content not found.")
  '''

if __name__=="__main__":  
  main()
