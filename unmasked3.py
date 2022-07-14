import urllib.request
import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

pagesToGet = 1

upperframe = []
for page in range(1, pagesToGet+1):
    print('processing page :', page)
    url = 'https://www.politifact.com/factchecks/list/?page='+str(page)
    print(url)

    # an exception might be thrown, so the code should be in a try-except block
    try:
        # use the browser to get the url. This is suspicious command that might blow up.
        # this might throw an exception if something goes wrong.
        page = requests.get(url)

    except Exception as e:                                   # this describes what to do if an exception is thrown
        # get the exception information
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)  # print the link that cause the problem
        # print error info and line that threw the exception
        print(error_type, 'Line:', error_info.tb_lineno)
        continue  # ignore this page. Abandon this and go back.
    time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    frame = []
    links = soup.find_all('li', attrs={'class': 'o-listicle__item'})
    print(len(links))
    filename = "NEWS.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement,Link,Date, Source, Label\n"
    f.write(headers)

    for j in links:
        Statement = j.find(
            "div", attrs={'class': 'm-statement__quote'}).text.strip()
        Link = "https://www.politifact.com"
        Link += j.find("div", attrs={'class': 'm-statement__quote'}
                       ).find('a')['href'].strip()
        Date = j.find('div', attrs={
                      'class': 'm-statement__body'}).find('footer').text[-14:-1].strip()
        Source = j.find(
            'div', attrs={'class': 'm-statement__meta'}).find('a').text.strip()
        Label = j.find('div', attrs={'class': 'm-statement__content'}).find(
            'img', attrs={'class': 'c-image__original'}).get('alt').strip()
        frame.append(Statement)
        f.write(Statement.replace(",", "^")+"\n")
    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement'])
data.head()
