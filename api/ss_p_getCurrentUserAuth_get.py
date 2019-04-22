#coding=utf8
import requests
from read import url_post
from read import headers

#获取当前用户权限
def ss_p_getCurrentUserAuth_get():
    body = {

    }

    url = url_post() + 'p_getCurrentUserAuth'
    r = requests.get(url,headers=headers())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_p_getCurrentUserAuth_get()