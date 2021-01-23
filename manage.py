import json


def open_data():
    try:
        with open('数据管理.txt','r',encoding='gbk') as f:
            data = f.read()
        return data
    except:
        with open('数据管理.txt','r',encoding='utf-8') as f:
            data = f.read()
        return data


def sava_data(jsonData):
    with open('数据管理.txt','w+') as f:
        f.write(str(jsonData).replace("'",'"'))

def add_data():
    stuNo = input('请输入添加人的学号')
    name = input('请输入添加人的姓名')
    jsonData[stuNo] = {"stuNo": stuNo,
                       "name": name
                       }

def del_data():
    stuNo = input("请输入你要删除的学号")
    del jsonData[stuNo]

def serchData():
    stuNo = input("请输入你要查找的学号")
    try:
        print(jsonData[stuNo])
    except:
        print("查无此人")
if __name__ == '__main__':
    print("1、添加\n"
          "2、删除\n"
          "3、查找\n"
          "4、退出并保存")
    jsonData = json.loads(open_data())
    while True:
        temp = input("请输入所需功能序号")
        if temp=='1':
            add_data()
            print(jsonData)
        elif temp=='2':
            del_data()
        elif temp=='3':
            serchData()
        elif temp=='4':
            sava_data(jsonData)
            break









