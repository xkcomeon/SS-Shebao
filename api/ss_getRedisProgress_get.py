#coding:utf-8

import requests
import read


#获取下载进度
def ss_getRedisProgress_get():
    body = {
        "fileKey":"SS_daily_USERS_INSURED_INFOS_EXPORT-ding118245741eb85d1135c2f4657eb6378f-1542960114841"
    }

    url = read.url_post() + 'getRedisProgress'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getRedisProgress_get()



