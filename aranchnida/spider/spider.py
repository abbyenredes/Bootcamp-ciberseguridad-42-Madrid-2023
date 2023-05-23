 #!/usr/bin/env python3
  2
  3 #libraries
  4 import requests
  5 from bs4 import BeautifulSoup as bs
  6 import os
  7 import argparse
  8 from urllib.parse import urlparse
  9
 10 #Function for the arguments
 11 parser = argparse.ArgumentParser() #object of ArgumentParser
 12 #add arguments to the  object
 13 parser.add_argument('url', help='Enter the  web to \'scrape\'', type=str)
 14 parser.add_argument('-r', '--recursive', help='Images will be downloaded recursively', action='store_true')
 15 parser.add_argument('-l', '--depth', help='Depth level for searching and downlanding images', type=int, default=5)
 16 parser.add_argument('-p', '--path', help='Folder where the images will be downloaded',type=str, default='./data/')
 17
 18 args = parser.parse_args() #Parse the arguments
 19
 20 #Web request
 21 def scraping(web_site, level):
 22         try:
 23
 24                 req = requests.get(web_site, timeout=5)
 25
 26                 #Check the request
 27                 status_code = req.status.get(web_site)
 28                 if status_code == 200:
 29                         soup = bs(req.text, 'html.parser') #Pass the HTML content to a  BS object
 30                         links = soup.find_all('a')#I go through all the entries of the web to extract the img
 31                         for link in links:
 32                                 print(i)
 33         finally:
 34                 print(error)
 35
 36 scrapear(url, depth)
