# -*- coding:utf-8 -*-
import json
import random
import requests
import sys

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/62.0.3202.75 Safari/537.36'}

    pro_list = [{'http': '119.98.71.99:8118'},
                {'http': '124.237.112.100:8088'},
                {'http': '59.62.25.4:48888'},
                {'http': '118.122.92.252:37901'},
                {'http': '122.114.31.177:808'},
                {'http': '61.135.217.7:80'},
                {'http': '218.88.215.157:808'},
                {'http': '218.73.134.234:36602'},
                {'http': '121.69.13.242:53281'},
                {'http': '125.122.169.7:61234'},
                {'http': '58.216.61.230:6666'},
                {'http': '106.122.170.241:8118'},
                {'http': '125.118.79.44:6666'},
                {'http': '117.94.114.196:61234'},
                {'http': '125.118.151.214:6666'},
                {'http': '36.24.72.153:8118'},
                {'http': '222.76.187.167:8118'},
                {'http': '114.232.113.99:8118'},
                {'http': '49.83.190.68:61234'},
                {'http': '221.224.49.237:3128'},
                {'http': '113.86.220.201:808'},
                {'http': '175.5.46.116:808'},
                {'http': '120.92.102.240:10000'},
                {'http': '60.189.195.18:808'},
                {'http': '120.92.117.188:10000'}
                ]
    proxy = random.choice(pro_list)
    print(str(proxy)+"       "+str(url))
    type = sys.getfilesystemencoding()
    s = requests.session()
    response = s.get(url, verify=False,headers=headers, proxies=proxy, timeout=30)
    html = response.text
    response.close()
    return html


def jd_price(url):
    try:
        sku = url.split('/')[-1].strip(".html")
        print(sku)
        price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku
        try:
            content = get_html(price_url)
        except:
            content = get_html(price_url)
        result = json.loads(content)
        print(result)
        record = result[0]
        return record['p']
    except KeyError:
        print('KeyError')
        return KeyError


def get_comment_num(phone_id):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId=' \
          + str(phone_id) + '&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&fold=1'
    try:
        html = get_html(url)
    except:
        html = get_html(url)
    jsondata = html[27:-2]
    data = json.loads(jsondata)

    return data['productCommentSummary']['commentCount']


if __name__ == "__main__":
    get_comment_num('18238476483')
