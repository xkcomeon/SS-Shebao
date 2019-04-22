#coding:utf-8

import requests
import read


#根据社保方案ID获取基数范围及最早时间
def ss_getBaseAndDateBySchemeId_get():
    body = {
        "schemeId":read.ss_schemeId(),  #获取上海社保唯一标准
        "type":1   #1:社保 2:公积金
    }

    url = read.url_post() + 'getBaseAndDateBySchemeId'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getBaseAndDateBySchemeId_get()



