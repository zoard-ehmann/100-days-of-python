import requests
from bs4 import BeautifulSoup


with requests.Session() as session:
    response = session.get('https://news.ycombinator.com/news')

yx_web_page = response.text

soup = BeautifulSoup(yx_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_upvote = max(article_upvotes)
index = article_upvotes.index(largest_upvote)

print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])
