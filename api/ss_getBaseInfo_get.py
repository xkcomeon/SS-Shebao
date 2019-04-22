#coding:utf-8

import requests
from read import url_post
from read import header
from read import userId



#获取基本信息
def ss_getBaseInfo_get():
    body = {
	"userId":userId(),
	"isHiddenMobile": "true",     #true:隐藏手机号  false：不隐藏，可编辑
	"isHiddenIdCard": "true"     #true:隐藏身份证  false：不隐藏，可编辑
}

    url = url_post() + 'getBaseInfo'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getBaseInfo_get()




