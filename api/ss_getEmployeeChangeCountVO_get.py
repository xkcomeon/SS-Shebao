#conding=utf8
import requests
from read import url_post
from read import header

#每月变动人员数--在职、离职
def ss_getEmployeeChangeCountVO_get():
    body = {
        #在职员工社保增员：      离职员工
        "employeeChangeKey": "SS_INSURING",  # 社保在职正常在缴的员工     社保正常在缴离职员工：SS_INSURING~DIMISSION
        "page": 1,
        "pageSize": 10
    }

    url = url_post() + 'getEmployeeChangeCountVO'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getEmployeeChangeCountVO_get()


