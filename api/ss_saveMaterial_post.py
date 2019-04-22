#coding:utf-8

import requests
import read


#保存员工线上材料
def ss_saveMaterial_post():
    body = {
        "userId":read.userId(),
        "list": [
            {
                "fieldKey": "1",
                "fieldValue": "import/2018/11/22/1542886258011/ding118245741eb85d1135c2f4657eb6378f_manager914_032185147a224bb92e70795ee7b2dddf.jpeg"
            },
            {
                "fieldKey": "2",
                "fieldValue": "import/2018/11/22/1542886262309/ding118245741eb85d1135c2f4657eb6378f_manager914_4d3173c92ae1ddb231e1b559dafcef79.jpg"
            }
        ]
    }

    url = read.url_post() + 'saveMaterial'
    r = requests.post(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_saveMaterial_post()



