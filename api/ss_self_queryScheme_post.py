# coding=utf8

import requests
from read import url_post
from read import header


# 查询参保方案列表
def ss_self_queryScheme_post():
    body = {
        "cityCode": "",
        "page": 1,
        "pageSize": 30
    }

    url = url_post() + 'self_queryScheme'
    r = requests.get(url, json=body, headers=header())

    # 获取返回值
    print(r.text)
    # 获取返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_self_queryScheme_post()
