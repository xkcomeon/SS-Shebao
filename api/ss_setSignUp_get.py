#coding:utf-8

import requests
import read


#新手引导的提交报名接口（手机端）
def ss_setSignUp_get():
    body = {
        "userName": "张三",
        "mobile": "122323243432",
        "corpSize":"1-50"
    }

    url = read.url_post() + 'setSignUp'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_setSignUp_get()



