# -*- coding: utf8 -*-
import requests,json,os
from campus_card import open_device, CampusCard
#修改完美校园打卡用户信息认证

def alter_user(class_id,name,stuNo,token):
    data ={'collegeId':'年纪id',
            'majorId':'专业id',
            'classId':class_id,
            'classDescription':'',
            'username':name,
            'stuNo':stuNo,
            'appClassify':'DK',
            'token':token
           }
    headers = {"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Length": "42","Content-Type": "application/x-www-form-urlencoded;charset=UTF-8","Cookie": "_ga=GA1.2.6099092.1604072758; _gid=GA1.2.1584202595.1604072758; Hm_lpvt_e6dc8d4ff407fa31b8604fc21fb115bc=1604072774; Hm_lvt_e6dc8d4ff407fa31b8604fc21fb115bc=1604072757,1604072774; shiro.session=d6c7039f-da19-4d92-9032-4555c8dc6f0d; _gat=1; sid=cnhHYlk5WHQteGI2WC1ZUEFiLVpHYlctOVdCQzZDeFBaQVpi","Host": "reportedh5.17wanxiao.com","Origin": "https://reportedh5.17wanxiao.com","Referer": "https://reportedh5.17wanxiao.com/collegeHealthPunch/index.html?token=38674e50-87c5-42b7-967f-efdaca829b97","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Wanxiao/5.3.2",}
    url = 'https://reportedh5.17wanxiao.com/api/clock/school/saveUserInfo'
    response = requests.post(url,data=data,headers=headers).text
    print(response)

#实现打卡
def sign_school(deptid,stuNo,name,token):
    url_epmpics = 'https://reportedh5.17wanxiao.com/sass/api/epmpics'
    s = requests.session()
    try:
        data_information_1 = {
                "businessType": "epmpics",
                "method": "submitUpInfoSchool",
                "jsonData": {
                    "deptStr": {
                        "deptid": deptid,
                        "text": ''
                    },
                    "areaStr": "{\"province\":\"河南省\",\"city\":\"新乡市\",\"district\":\"牧野区\",\"streetNumber\":\"32号\",\"street\":\"建设东路\",\"pois\":\"河南师范大学(西区)\",\"lng\":\"113.912703\",\"lat\":\"35.328507\",\"address\":\"牧野区建设东路32号河南师范大学(西区)\",\"text\":\"河南省-新乡市\",\"code\":\"\"}",
                    "reportdate": 1603408953292,
                    "customerid": 206,
                    "deptid": deptid,
                    "source": "alipay",
                    "templateid": "clockSign1",
                    "stuNo": stuNo,
                    "username": name,
                    "userid": 144,
                    "updatainfo": [
                        {
                            "propertyname": "temperature",
                            "value": "36.8"
                        },
                        {
                            "propertyname": "symptom",
                            "value": "无症状"
                        },
                        {
                            "propertyname": "dormitory",
                            "value": "西区"
                        }
                    ],
                    "customerAppTypeRuleId": 341,
                    "clockState": 0,
                    "token": token
                },
                "token": token
            }

        resp_1 = s.post(url_epmpics, json=data_information_1).json()['msg']
        print(resp_1)
        return resp_1
    except:
        print('代码错误')

def get_token():
    campus = CampusCard("账号", "密码", open_device('userinfo.txt'))
    bills = campus.get_bill("2019-06-01", "2019-07-31")
    with open('userinfo.txt') as f:
        json_1 = json.loads(f.read())
        print(json_1['sessionId'])
    os.remove('userinfo.txt')
    return json_1['sessionId']
#Q酱推送打卡信息
def informations_push(msg):
    skey = ''
    url = 'https://qmsg.zendee.cn/group/' + skey + '?msg='+msg
    requests.get(url)

if __name__ == '__main__':
    url_server = ''
    name = ['张三']
    stuNo =['190000000']
    token = get_token()
    for i in range(0,len(name)):
        alter_user('班级id',name[i],stuNo[i],token)
        url_server=url_server+name[i]+'--->'+sign_school("班级id",stuNo[i],name[i],token)+'\n'
    requests.get(url_server)
    os.remove('userinfo.txt')
