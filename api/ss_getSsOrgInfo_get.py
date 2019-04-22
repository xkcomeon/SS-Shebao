#conding=utf8
import requests
from read import url_post
from read import header

#获取账户（大库和单立户）列表
def ss_getSsOrgInfo_get():
    body = {

    }

    url = url_post() + 'getSsOrgInfo'
    r = requests.get(url,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getSsOrgInfo_get()


