#coding:utf-8

import requests
import read


#获取社保方案详情
def ss_getSchemeDetail_get():
    body = {
        "schemeId":read.ss_schemeId(),  #上海社保唯一标准
        "payMonth": "2018-12"
    }

    url = read.url_post() + 'getSchemeDetail'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getSchemeDetail_get()



