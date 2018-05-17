# -*- coding: utf-8 -*-
import threading
import json
import time
import urllib.request
import urllib.error
import socket

exitFlag = 0


def crawlProductComment(link, goods_id):
    try:
        contents = urllib.request.urlopen(link, timeout=100)
        print(link)
        html = contents.read().decode('gbk')
        jsondata = html[27:-2]
        data = json.loads(jsondata)
        # 遍历商品评论列表
        try:
            for comment in data['comments']:
                product_name = comment['referenceName']  # 商品名
                comment_time = comment['creationTime']  # 创建时间
                content = comment['content']    # 评论内容
                # 输出商品评论关键信息
                print("商品全名:{}".format(product_name))
                print("用户评论时间:{}".format(comment_time))
                print("用户评论内容:{}".format(content))
                print("-----------------------------")
                with open('F:\\PythonFile\\Recommend\\app\\spider\\comment\\%s.txt'%goods_id,'a') as f:
                    f.write(str([ product_name,comment_time,content]))
                    f.write('\n')
                # mysql.save_comments2(ids, goods_id, product_name, comment_time, content)
        except:
            pass
        contents.close()
    except socket.timeout:
        contents = urllib.request.urlopen(link)
        print(link)
        html = contents.read().decode('gbk')
        jsondata = html[27:-2]
        data = json.loads(jsondata)
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
            with open('F:\\PythonFile\\Recommend\\app\\spider\\comment\\%s.txt' % goods_id, 'a') as f:
                f.write(str([product_name, comment_time, content]))
                f.write('\n')
        contents.close()

class myThread (threading.Thread):
    def __init__(self, page_num,goods_id):
        threading.Thread.__init__(self)
        self.url ='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId='\
              + str(goods_id) + '&score=0&sortType=5&page=' + str(page_num) + '&pageSize=10&isShadowSku=0&fold=1'
        self.goods_id = goods_id

    def run(self):
        print ("开始线程：" + self.url)
        crawlProductComment(self.url,self.goods_id)

#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

def start_thread(n,goods_id):
    thread1 = myThread(n, goods_id)
    thread2 = myThread(n+1, goods_id)
    thread3 = myThread(n+2, goods_id)
    thread4 = myThread(n+3, goods_id)
    thread5 = myThread(n+4, goods_id)
    thread6 = myThread(n+5, goods_id)
    thread7 = myThread(n+6, goods_id)
    thread8 = myThread(n+7, goods_id)
    thread9 = myThread(n+8, goods_id)
    thread10 = myThread(n+9, goods_id)
    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    print("退出主线程")
if __name__ == "__main__":
    for n in range(1,100,10):
        start_thread(n,4120323)

