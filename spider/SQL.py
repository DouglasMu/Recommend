# coding:utf-8
from math import ceil

import pymysql


# 将得到的数据存入数据库中mysql
class save_mysql:
    def __init__(self):
        self.user = 'root'
        self.password = 'admin'
        self.host = 'localhost'
        self.database2 = 'recommend'
        self.database1 = 'recommend_data'

    def save_link(self, i, url):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host,
                               db=self.database1, charset="utf8")
        cursor = conn.cursor()
        sql = "insert into netbook_url(id, url) values(%s ,%s)"
        cursor.execute(sql, (i, url))   # url插入到数据库中
        conn.commit()
        conn.close()

    def read_link(self, phoneid):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host,
                               db=self.database1, charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT url from phone_url where id = %s"
        cursor.execute(sql % phoneid)
        link = cursor.fetchall()
        conn.close()
        return link

    def save_comment(self, pid, name, price, com_num, phone_id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host,
                               db=self.database2, charset="utf8")
        cursor = conn.cursor()
        sql="insert into app_goods(id, goods_name, price, comment_num, goods_id) " \
            "VALUES (%s, %s, %s, %s, %s)"
        # print(sql%(pid,name, price,com_num,phone_id))
        cursor.execute(sql,(pid,name, price,com_num,phone_id))
        conn.commit()
        conn.close()