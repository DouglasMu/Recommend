# -*- coding: utf-8 -*-
import json
import time
import urllib.request
import urllib.error
import pymysql
import socket
import get_comment.SQL


def crawlProductComment(link, ids, goods_id):
    try:
        contents = urllib.request.urlopen(link, timeout=100)
        print(link)
        html = contents.read().decode('gbk')
        jsondata = html[27:-2]
        # print(jsondata)
        data = json.loads(jsondata)
        # print(data['productCommentSummary']['commentCount'])
        # 遍历商品评论列表
        for comment in data['comments']:
            product_name = comment['referenceName']  # 商品名
            comment_time = comment['creationTime']  # 创建时间
            content = comment['content']    # 评论内容
            # 输出商品评论关键信息
            print("商品全名:{}".format(product_name))
            print("用户评论时间:{}".format(comment_time))
            print("用户评论内容:{}".format(content))
            print("-----------------------------")
            mysql.save_comments2(ids, goods_id, product_name, comment_time, content)
            ids = ids+1
        contents.close()
    except socket.timeout:
        contents = urllib.request.urlopen(link)
        print(link)
        html = contents.read().decode('gbk')
        jsondata = html[27:-2]
        # print(jsondata)
        data = json.loads(jsondata)
        # print(data['productCommentSummary']['commentCount'])
        # 遍历商品评论列表
        for comment in data['comments']:
            product_name = comment['referenceName']  # 商品名
            comment_time = comment['creationTime']  # 创建时间
            content = comment['content']  # 评论内容
            # 输出商品评论关键信息
            print("商品全名:{}".format(product_name))
            print("用户评论时间:{}".format(comment_time))
            print("用户评论内容:{}".format(content))
            print("-----------------------------")
            mysql.save_comments2(ids, goods_id, product_name, comment_time, content)
            ids = ids + 1
        contents.close()


def comment_execute(goods_id):
    ids = 1
    for iss in range(0, 100):
        print("正在获取第{}页评论数据!".format(iss+1))
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId='\
              + str(goods_id) + '&score=0&sortType=5&page=' + str(iss) + '&pageSize=10&isShadowSku=0&fold=1'
        crawlProductComment(url, ids, goods_id)
        time.sleep(1)
        ids = ids + 10


if __name__ == "__main__":
    mysql = get_comment.SQL.save_mysql()

    for i in range(511, 21167, 2):
        try:
            print(i)
            phone_id = mysql.read_phone_info(i)
            if phone_id == 0:
                continue
            else:
                print(phone_id)
                mysql.save_comments1(phone_id)
                comment_execute(phone_id)
        except TimeoutError:
            print("连接超时")
            mysql.save_error(phone_id, "连接超时")
        except urllib.error.HTTPError :
            print("HTTPError")
            mysql.save_error(phone_id, "网址错误")
        except urllib.error.URLError:
            print("HTTPError")
            mysql.save_error(phone_id, "网址错误")
        except UnicodeDecodeError:
            print("UnicodeError")
            mysql.save_error(phone_id, "编码错误")
        except pymysql.err.InternalError:
            print("表已经存在")
        except TypeError:
            mysql.save_error(phone_id, "类型错误")

