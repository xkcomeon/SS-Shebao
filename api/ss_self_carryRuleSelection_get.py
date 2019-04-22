#coding=utf8

import requests
from read import url_post
from read import header

#参保方案获取进位规则
def ss_self_carryRuleSelection_get():
    body = {

    }

    url = url_post() + 'self_carryRuleSelection'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_self_carryRuleSelection_get()