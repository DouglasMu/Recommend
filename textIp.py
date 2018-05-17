import socket
from urllib import request

import requests
import sys


def IPpool():
    IPpool = []
    with open('F:\\PythonFile\\Recommend\\test.txt','r') as file:
            line = file.readline()
            while line:
                # print(line)
                line = file.readline()
                line = line.replace('[b\'','').replace(' b\'','').replace('\']','').replace('\n','').replace('\'','')
                line=line.split(',')

                try:
                    proxy1 = {}
                    proxy1['http'] = line[0] + ':' + line[1]
                    print(dict(proxy1))
                    type = sys.getfilesystemencoding()
                    s = requests.session()
                    url = 'http://www.whatismyip.com.tw/'
                    print(url)
                    response = s.get(url, verify=False, proxies=dict(proxy1), timeout=4)
                    print(response.text)
                    with open('F:\\PythonFile\\Recommend\\ip.txt','a') as f:
                        f.write(str(proxy1))
                        f.write('\n')

                    print("可用IP："+str(proxy1))
                except:
                    print("----不可用")
                    continue
    print(IPpool)
if __name__ =="__main__":
    IPpool()