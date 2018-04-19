# -*- coding:utf-8 -*-
import json
import urllib.request
import requests


def jd_price(url):
    try:
        sku = url.split('/')[-1].strip(".html")
        price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku
        responses = urllib.request.urlopen(price_url)
        content = responses.read()
        result = json.loads(content)
        record = result[0]
        responses.close()
        return record['p']
    except KeyError:
        print('KeyError')
        return KeyError


def get_comment_num(phone_id):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId=' \
          + str(phone_id) + '&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&fold=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/62.0.3202.75 Safari/537.36'}
    contents = requests.get(url, headers=headers)
    html = contents.text
    jsondata = html[27:-2]
    data = json.loads(jsondata)
    contents.close()
    return data['productCommentSummary']['commentCount']


if __name__ == "__main__":
    get_comment_num('18238476483')