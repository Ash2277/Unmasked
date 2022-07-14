from requests.sessions import session
from requests_html import HTMLSession
session = HTMLSession()
url = 'https://twitter.com/explore/tabs/news_unified'

r = session.get(url)

r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('div')
print(articles)
for item in articles:
    newsitem = item.find('span', first=True)
    title = newsitem.text
    print(title)
