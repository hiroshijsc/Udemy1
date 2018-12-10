from bs4 import BeautifulSoup
import requests
import pandas as pd
columns = ['rank', 'title', 'url', 'affeliate_url']
df = pd.DataFrame(columns = columns)
df.head()
html_doc = requests.get('https://www.google.co.jp/search?num=10&q=' + keyword)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
