#coding:utf-8

import requests
import read


#在新手引导结束后调用该该接口
def ss_setNewerGuide_get():
    body = {
        "type": 2      #pc端不改，手机端：2
    }

    url = read.url_post() + 'setNewerGuide'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_setNewerGuide_get()



