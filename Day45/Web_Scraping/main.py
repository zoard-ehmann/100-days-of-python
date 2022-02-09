# import lxml
from bs4 import BeautifulSoup


with open('Day45/Web_Scraping/website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
    break
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id='heading')
# print(heading)

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.get('class'))

name = soup.select_one(selector='#name')
# print(name)

headings = soup.select(selector='.heading')
# print(headings)