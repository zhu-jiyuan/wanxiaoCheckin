import requests,json,os,time,random
from campus_card import open_device, CampusCard

#更换打卡的人,并打卡

def updata_information(data,token):
    url = 'https://reportedh5.17wanxiao.com/sass/api/epmpics'
    areaStr=str(data["areaStr"]).split("-")
    address = str(areaStr[2])
    texts=str(areaStr[0])+'-'+str(areaStr[1])
    data = {
        "businessType": "epmpics",
        "method": "submitUpInfo",
        "jsonData": {
            "add": "false",
            "areaStr": "{\"address\":\""+address+"\",\"text\":\""+texts+"\"}",
            "cardNo": 'null',
            "customerid": "206",
            "deptStr": {
                "deptid": data["deptid"],
                "text": data["deptStr"]
            },
            "phonenum": data["ownPhone"],
            "stuNo": data["stuNo"],
            "templateid": "pneumonia",
            "upTime": 'null',
            "userid": data["userid"],
            "username": data["username"],
            "deptid": data["deptid"],
            "updatainfo": [
                {
                    "propertyname": "temperature",
                    "value": "36."+str(random.randint(4,8))
                },
                {
                    "propertyname": "symptom",
                    "value": "无症状"
                },
                {
                    "propertyname": "isConfirmed",
                    "value": "否"
                },
                {
                    "propertyname": "isdefinde",
                    "value": "否.未隔离"
                },
                {
                    "propertyname": "isTouch",
                    "value": "否"
                },
                {
                    "propertyname": "isTransitArea",
                    "value": "否"
                },
                {
                    "propertyname": "是否途径或逗留过疫情中，高风险地区？",
                    "value": "否"
                },
                {
                    "propertyname": "isFFHasSymptom",
                    "value": "没有"
                },
                {
                    "propertyname": "isContactFriendIn14",
                    "value": "没有"
                },
                {
                    "propertyname": "xinqing",
                    "value": "健康"
                },
                {
                    "propertyname": "bodyzk",
                    "value": "是"
                },
                {
                    "propertyname": "cxjh",
                    "value": "否"
                },
                {
                    "propertyname": "isleaveaddress",
                    "value": "否"
                },
                {
                    "propertyname": "isAlreadyInSchool",
                    "value": "没有"
                },
                {
                    "propertyname": "ownPhone",
                    "value": data["ownPhone"]
                },
                {
                    "propertyname": "emergencyContact",
                    "value": data["emergencyContact"]
                },
                {
                    "propertyname": "mergencyPeoplePhone",
                    "value": data["mergencyPeoplePhone"]
                },
                {
                    "propertyname": "assistRemark",
                    "value": ""
                }
            ],
            "source": "alipay",
            "reportdate": int(time.time() * 1000),
            "gpsType": 1,
            "token": token
        }
    }
    headers = {
               "Host": "reportedh5.17wanxiao.com",
               "Referer": "https://reportedh5.17wanxiao.com/health/index.html?templateid=pneumonia&businessType=epmpics&token="+token+"c&customerId=206&fromincollege=1",
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 Ariver/1.1.0 AliApp(AP/10.2.10.6010) Nebula WK RVKType(1) AlipayDefined(nt:4G,ws:375|603|2.0) AlipayClient/10.2.10.6010 Language/zh-Hans Region/CN MiniProgram APXWebView NebulaX/1.0.0",}
    responses = requests.post(url,json=data,headers=headers).json()['msg']
    return responses

#Q酱推送打卡信息
def informations_push(msg):
    #填自己的key
    skey = ''
    url = 'https://qmsg.zendee.cn/group/' + skey + '?msg='+msg
    requests.get(url)

def get_token():
    campus = CampusCard("app账号", "密码", open_device('userinfo.txt'))
    campus.get_main_info()
    with open('userinfo.txt') as f:
        json_1 = json.loads(f.read())
        print(json_1['sessionId'])
    os.remove('userinfo.txt')
    return json_1['sessionId']
def token_sure(token):
    json_data = {
        "businessType": "epmpics",
        "jsonData": {
            "templateid": "pneumonia",
            "token": token
        },
        "method": "getUpDataInfoDetail"
    }
    headers = {
               "Host": "reportedh5.17wanxiao.com",
               "Referer": "https://reportedh5.17wanxiao.com/health/index.html?templateid=pneumonia&businessType=epmpics&token="+token+"c&customerId=206&fromincollege=1",
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 Ariver/1.1.0 AliApp(AP/10.2.10.6010) Nebula WK RVKType(1) AlipayDefined(nt:4G,ws:375|603|2.0) AlipayClient/10.2.10.6010 Language/zh-Hans Region/CN MiniProgram APXWebView NebulaX/1.0.0",}
    requests.post('https://reportedh5.17wanxiao.com/sass/api/epmpics',json=json_data,headers=headers)

if __name__ == '__main__':
    #获取token
    token = get_token()
    token_sure(token)
    try:
        with open('打卡数据.txt','r',encoding='utf-8') as f:
            data = json.loads(f.read())
    except:
        with open('打卡数据.txt','r',encoding='gbk') as f:
            data = json.loads(f.read())

    try:
        with open('数据管理.txt','r',encoding='utf-8') as j:
            list_1 = json.loads(j.read())
    except:
        with open('数据管理.txt','r',encoding='gbk') as j:
            list_1 = json.loads(j.read())
    msg = '健康打卡详情：\n'
    for stuNo in list_1.keys():
        if updata_information(data[stuNo],token)=='成功':
            msg=msg+list_1[stuNo]["name"]+'--->'+'成功'+'\n'
        else:
            time.sleep(60*5)
            if updata_information(data[stuNo], token) == '成功':
                msg = msg + list_1[stuNo]["name"] + '--->' + '成功' + '\n'
            else:
                msg = msg + list_1[stuNo]["name"] + '--->' + '业务异常' + '\n'
        # time.sleep(random.randint(0,15))
    informations_push(msg)


