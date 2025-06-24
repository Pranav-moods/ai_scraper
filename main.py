from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

URL="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"


with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page()
    page.goto(URL)
    page.screenshot(path="ch1.png")
    browser.close()


response=requests.get(URL)
soup=BeautifulSoup(response.content,"html.parser")
content=soup.find("div",{"class":"mw-parser-output"})
text=content.get_text(separator='\n',strip=True)


with open("ch1.txt", "r", encoding="utf-8") as f:
    text = f.read()

