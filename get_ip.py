import requests
from bs4 import BeautifulSoup

import csv


def IPspider(numpage):
    list1 = []

    url = 'http://www.xicidaili.com/nn/'
    user_agent = 'IP'
    headers = {'User-agent': user_agent}
    for num in range(1, numpage + 1):
        ipurl = url + str(num)
        print('Now downloading the ' + str(num * 100) + ' ips')
        request = requests.get(ipurl, headers=headers)
        content = request.text
        bs = BeautifulSoup(content, 'html.parser')
        res = bs.find_all('tr')
        for item in res:
            try:
                temp = []
                tds = item.find_all('td')
                temp.append(tds[1].text.encode('utf-8'))
                temp.append(tds[2].text.encode('utf-8'))
                list1.append(temp)
            except IndexError:
                pass

                # 假设爬取前十页所有的IP和端口
    with open('F:\\PythonFile\\Recommend\\test.txt','a') as file:
        for i in list1:
            file.write(str(i))
            file.write("\n")

IPspider(10)