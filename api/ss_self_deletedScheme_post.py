# coding=utf8

import requests
from read import url_post
from read import header


# 获取详细参保方案信息
def ss_self_deletedScheme_post():
    body = {
        "ssSchemeId":"8fd65ccde0eb41c4a94eda8f52fb3625",  #社保方案id
        "hfSchemeId":"37a72edf11bb4795aae2d9db406df24b",  #公积金方案id
    }

    url = url_post() + 'self_deletedScheme'
    r = requests.get(url, json=body, headers=header())

    # 获取返回值
    print(r.text)
    # 获取返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_self_deletedScheme_post()
