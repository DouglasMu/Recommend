# coding:utf8
import os

import pandas as pd
from jieba.analyse import extract_tags
from snownlp import SnowNLP

# 获取关键词（名词）

with open('F:\\PythonFile\\JD_spider\\analysis\\phone_feature.txt') as f:
    features = list(f.read().split())


def features_analysis(file_name):
    file_path = "F:\\PythonFile\\jd\phone\\" + file_name
    mingci = ['n', 'ng', 'nz', 'nl']
    with open(file_path, 'r+') as phone:
        phone_content = phone.read().split('}')
    comment_list = []
    features_list = []
    feature_list = []
    for i in phone_content:
        # i = i[:-1]
        i = i + '}'
        if i is not '}':
            try:
                comment_list.append(eval(i))
            except:
                print("转换为字典操作失败：\n")

    for phone_dic in comment_list:
        for key, value in phone_dic.items():
            # print(key,value)
            if value in mingci:
                features_list.append(key)
    # print(features_list)
    for key, weight in extract_tags(str(features_list), 50, withWeight=True):
        # print(key,weight)
        feature_list.append(key)
    return (feature_list, features)


def sentiment_analysis(list_feature, features_list):  # 高频 ， 所有
    data = {}
    feat = pd.DataFrame()
    for i in range(0, len(features_list) - 1):
        if features_list[i] in list_feature:
            try:
                s1 = SnowNLP(str(features_list[i + 1])).sentiments
                s2 = SnowNLP(str(features_list[i + 2])).sentiments
                # print(s1,s2)
                if features_list[i] not in data:
                    data[features_list[i]] = [(s1 + s2), 2]
                else:
                    data[features_list[i]] = [(data[features_list[i]][0] + s1 + s2),
                                              data[features_list[i]][1] + 2]
            except IndexError:
                continue
    return data


def get_result():
    file_list = os.listdir("F:\\PythonFile\\jd\\phone")
    result = {}
    for filename in file_list:
        list_feature = []
        # print(filename)
        id = filename.split('.')[0]
        print(id)
        (features_list, list_1) = features_analysis(filename)  # 所有的词 ， 高频词
        for list_2 in features_list:
            if list_2 in features:
                list_feature.append(list_2)
        data = sentiment_analysis(list_1, features_list)
        data1 = {}
        for key, value in data.items():
            data1[key] = value[0] / value[1]
        data11 = sorted(data1.items(), key=lambda item: item[1], reverse=True)
        result[id] = data11
    return result


if __name__ == '__main__':
    dic = get_result()
    print(dic)
