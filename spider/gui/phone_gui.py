import easygui as g
import matplotlib.pyplot as plt
import numpy as np

from spider.analysis import phone_analysis1 as pa
from spider.search import phone_search as ps


def search():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    result = pa.get_result()
    g.msgbox("欢迎进入商品评论分析系统")
    title = "商品查询"
    phone_name = g.enterbox(msg="输入您要查询的手机名称",
                            title="商品查询")
    select_list = ps.search1(phone_name)
    list1 = []
    dic2 = {}
    dic3 = {}
    for dic in select_list:
        if dic['phoneid'] in result:
            phone_name1 = dic['phone_name']
            dic3[phone_name1] = dic["price"]  # 储存手机的价格
            list1.append(phone_name1)
            dic2[phone_name1] = result[dic['phoneid']]  # 存储手机的id
    while 1:
        item = g.choicebox(msg="请选择手机", choices=list1, title='商品选择')
        feature = []
        number = []
        for i in dic2[item]:
            feature.append(i[0])
            number.append((i[1] - 0.5) * 10)
        print(feature)
        # 取一张白纸
        fig = plt.figure(1)
        ax1 = plt.subplot(111)
        x_bar = np.arange(len(feature))
        rect = ax1.bar(x=x_bar, height=number, color='lightblue')
        ax1.set_title('特征柱状图')
        ax1.set_xticks(x_bar)
        ax1.set_xticklabels(feature)
        plt.show()
