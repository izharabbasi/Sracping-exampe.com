import requests

from bs4 import BeautifulSoup

page = requests.get("https://www.example.com/")

soup = BeautifulSoup(page.content,"html.parser")

print(soup.select_one("h1").string)
print(soup.select_one("p").string)
print(soup.select_one("p a").attrs["href"])
print(soup.select_one("p a").string)