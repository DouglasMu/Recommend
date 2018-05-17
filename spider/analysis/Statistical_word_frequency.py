# -*- coding:utf-8 -*-
import datetime
def word_frequency():
    word_dict = {}
    with open('F:\\PythonFile\\tingyongci.txt') as ti:
        ti_list = list(ti.read())   #   获取停用词表（综合哈工大停用词词表）
    with open('F:\\PythonFile\\jd\\phone\\3133927.txt') as wf:
        comments = list(wf.read().split())
        print(comments)
        for comment in comments:
            if comment in ti_list:
                continue
            else:
                if comment not in word_dict:
                    word_dict[comment] = int(1)
                else:
                    word_dict[comment] += 1
    file = open('F:\\PythonFile\\jd\\phone\\test.txt', mode='a')
    sorted(word_dict.items(), key=lambda item: item[1])
    for key in word_dict:
        print(key, word_dict[key])
        file.write(key + ' ' + str(word_dict[key]) + '\n')    # 写入文档
    file.close()
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    word_frequency()
    end_time = datetime.datetime.now()
    print("运行时间："+str(end_time-start_time))