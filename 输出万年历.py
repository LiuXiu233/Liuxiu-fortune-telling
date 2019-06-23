# -*- coding: UTF-8 -*-
# !/usr/bin/python3

import urllib
import urllib.request
import time
import base64
import json

#UUID采用当前程序运行时间，用于防止重放攻击，开发者可根据自己需求，自定义字符串
UUID = str(time.time())
#API产品路径
host = 'http://icalendar.market.alicloudapi.com'
path = '/ai_metaphysics/calendar/elite'
#阿里云APPCODE
appcode = '03ee092d9c6e4c89810f6daa327ee715' 

#参数配置
#时间，如：20180808080808，即2018年08月08日08时08分08秒，默认输入一天某个时间点，返回当天黄历数据
STRING = input("请输入时间(格式如:20180808080808)：")

querys = 'STRING=%s' %(STRING)
url = host + path + '?' + querys
request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('X-Ca-Nonce', UUID)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = json.loads(response.read())
result = content["艾科瑞特_老黄历"]
print (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False))
