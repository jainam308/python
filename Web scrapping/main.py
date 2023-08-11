# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data(content, encoding, status, etc).
import requests

# Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
# It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
#  It commonly saves programmers hours or days of work.
from bs4 import BeautifulSoup
url = "https://getbootstrap.com/"
r = requests.get(url)
html_content = r.content
# print(html_content)
soup = BeautifulSoup(html_content,'html.parser')
# print(soup.prettify)
title = soup.title
print(title)
# print(type(soup))
# paras = soup.find_all('p')
# print(paras)
# print(anchors)
# print(soup.find('p')['style']) 
# print(soup.find('p').get_text())
# anchors = soup.find_all('a')
# for link in anchors:
#  print(link)