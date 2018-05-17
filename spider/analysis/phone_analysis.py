# coding:utf-8
import datetime
import re
import string

import jieba.posseg as pseg
import zhon.hanzi

from spider.get_comment import SQL

#   要清洗掉的标点
ignoring_words = list(zhon.hanzi.punctuation)+list(string.punctuation)
#   数据库表中没有存储评论的表名称
ignoring_table = ['phone_info', 'phone_url', 'error_table','error_table1']


#   将分词后的数据储存到本地
def text_save(content, filename, mode='a'):
    file = open(filename, mode)
    file.write(str(content))    # 存储为str格式
    # 此处为存储为json格式
    # js = json.dumps(content)
    # file.write(js)
    file.close()


#   获取数据库中的评论
def get_comments(phones_id, i):
    mysql = SQL.save_mysql()    # 调用数据库操作
    comment = mysql.read_comment_phone(phones_id, i)
    for ob in comment:
        return str((ob[0]))


#   调用jieba分词包进行分词
def jieba_cut(phones_id, i):
    comment = get_comments(phones_id, i)
    comments_dict = dict(pseg.cut(comment))
    return comments_dict


#   获取数据库中的所有储存评论信息的表名
def get_phone_table():
    mysql = SQL.save_mysql()
    phone_id_list = list(mysql.select_all_table('jd_phone'))
    for table in phone_id_list:
        if table[0] in ignoring_table:
            phone_id_list.remove(table)
    phone_id_list.pop()
    return phone_id_list


#   调用其他函数完成数据的存储，格式为txt
def save_file(phone_id1):
    with open('F:\\PythonFile\\tingyongci.txt') as ti:
        ti_list = list(ti.read())  # 获取停用词表（综合哈工大停用词词表）
    for i in range(1, 1000):
        with open('F:\\PythonFile\\tingyongci.txt') as ti:
            ti_list = list(ti.read())  # 获取停用词表（综合哈工大停用词词表）
            try:
                new_dic = {}
                new_dic1 = jieba_cut(phone_id1, i)
                for key, value in new_dic1.items():
                    if key not in ti_list:
                        new_dic[key] = value
                    else:
                        pass
            except:
                continue
            print(new_dic)
            text_save(new_dic, 'F:\\data\\phone\\%s.txt' % phone_id1)
    print('----------------------id=%s---------------------------' % phone_id)


if __name__ == "__main__":
        start_time = datetime.datetime.now()
        phone_table_lists = get_phone_table()
        for phone_table_name in phone_table_lists:
            phone_id = re.sub("\D", "", phone_table_name[0])    # 获取表名中的phone_id
            save_file(int(phone_id))
            print("--------------id=%s--------------" % phone_id)
        end_time = datetime.datetime.now()
        print('运行时间：')
        print(end_time - start_time)
        # print(get_phone_table())
