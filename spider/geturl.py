import time

import requests
from bs4 import BeautifulSoup

from spider import SQL

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
                         ' Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/62.0.3202.75 Safari/537.36'}


def geturl(i,n, urlname):
    try:
        res = requests.get(urlname, headers=headers, timeout=100)
    except:
        res = requests.get(urlname, headers=headers)
    html = res.text
    # print html
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.findAll('a', target="_blank")
    for div in divs:
        link = div.get('href')
        print(link)
        if "//item.jd.com/" in link:
            sss = SQL.save_mysql()
            sss.save_link(i, link)
            i = i + 1

    res.close()
    time.sleep(1)
    print("page%s" % n)
    print("___________________________________________________________")
    return i


if __name__ == "__main__":
    i = 1
    phone_urls = "https://list.jd.com/list.html?cat=9987,653,655&page=%s"
    netbook_urls = "https://list.jd.com/list.html?cat=670,671,672&page=%s"

    for n in range(1, 1117):
        url = (netbook_urls % n)
        print(url)
        i = geturl(i, n, url)

