import requests
from bs4 import BeautifulSoup


def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text


url = ''
text = get_text(url)
print(text)
#print(text[:100])  # Первые 100 символов из строки