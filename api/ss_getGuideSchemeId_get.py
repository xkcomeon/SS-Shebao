#coding:utf-8

import requests
import read


#新手引导获取默认社保 公积金方案ID
def ss_getGuideSchemeId_get():
    body = {

    }

    url = read.url_post() + 'getGuideSchemeId'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getGuideSchemeId_get()



