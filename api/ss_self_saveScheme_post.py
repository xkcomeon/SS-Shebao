# coding=utf8

import requests
from read import url_post
from read import header


# 保存参保方案
def ss_self_saveScheme_post():
    body = {
        {
            "cityName": "上海",
            "cityCode": "310100",
            "serviceCharge": "",
            "ssInsureInfoModel": {
                "templateId": "f767f5f94f48419998294823ede91a81",
                "schemeId": "",
                "schemeName": "111",
                "corpTotalCarryRule": "1",
                "personTotalCarryRule": "1",
                "itemDetails": [
                    {
                        "itemCode": "insurancePension",
                        "itemName": "养老",
                        "corpBaseLower": "1000",
                        "corpBaseUpper": "5000",
                        "corpCarryRule": "1",
                        "corpFixedAmount": "100",
                        "corpPayRatio": "5",
                        "personCarryRule": "1",
                        "personFixedAmount": "150",
                        "personPayRatio": "6"
                    },
                    {
                        "itemCode": "insuranceMedical",
                        "itemName": "医疗",
                        "corpBaseLower": "1000",
                        "corpBaseUpper": "5000",
                        "corpCarryRule": "1",
                        "corpFixedAmount": "100",
                        "corpPayRatio": "5",
                        "personCarryRule": "1",
                        "personFixedAmount": "150",
                        "personPayRatio": "6"
                    },
                    {
                        "itemCode": "insuranceMaternity",
                        "itemName": "生育",
                        "corpBaseLower": "1000",
                        "corpBaseUpper": "5000",
                        "corpCarryRule": "1",
                        "corpFixedAmount": "100",
                        "corpPayRatio": "5",
                        "personCarryRule": "1",
                        "personFixedAmount": "150",
                        "personPayRatio": "6"
                    }
                ]
            },
            "hfInsureInfoModel": {
                "templateId": "f94d8548898411e8a13252540080f839",
                "schemeId": "",
                "schemeName": "1111",
                "corpTotalCarryRule": "1",
                "personTotalCarryRule": "1",
                "itemDetails": [
                    {
                        "itemCode": "insuranceHousingFund",
                        "itemName": "公积金",
                        "corpBaseLower": "2300",
                        "corpBaseUpper": "21396",
                        "corpCarryRule": "1",
                        "corpFixedAmount": "0",
                        "corpPayRatio": "7",
                        "personCarryRule": "1",
                        "personFixedAmount": "0",
                        "personPayRatio": "7"
                    }
                ]
            }
        }

    }

    url = url_post() + 'self_saveScheme'
    r = requests.post(url, json=body, headers=header())

    # 获取返回值
    print(r.text)
    # 获取返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_self_saveScheme_post()
