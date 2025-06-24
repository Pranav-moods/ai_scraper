import requests
from bs4 import BeautifulSoup

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

content_div = soup.find("div", class_="mw-parser-output")
paragraphs = content_div.find_all(["p", "h2", "h3", "ul", "ol", "li"])

chapter_text = "\n\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

print("Extracted Preview:\n", chapter_text[:1000])

with open("ch1.txt", "w", encoding="utf-8") as f:
    f.write(chapter_text)

print(" Chapter text saved to ch1.txt")
