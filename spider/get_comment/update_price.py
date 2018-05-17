# coding:utf8
import json

import requests

from spider.get_comment import SQL
from spider.get_comment.getprice import get_html
requests.packages.urllib3.disable_warnings()
for i in range(1,21300,2):

    sql = SQL.save_mysql()
    try:
        res = sql.read_phone_price(i)
        # print(res)
        # print("序号：" + str(i))
        if int(res[0][1]) == int(0):
            print("序号：" + str(i))
            try:
                price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + str(res[0][0])
                try:
                    content = get_html(price_url)
                except:
                    content = get_html(price_url)
                result = json.loads(content)
                record = result[0]
                price = int(float(record["p"]))
                print(price)
                sql.update_phone_price(i,price)
            except KeyError:
                print('KeyError')
    except IndexError:
        print('IndexError!!')