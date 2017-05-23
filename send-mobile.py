#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.web
import json
import sys
import urllib
import urllib2
import base64
import time
from  datetime import datetime
import json
import requests

####短信
def send_message_example(content,tos):
    resp = requests.post(("http://hy6.nbark.com:7602/sms.aspx?action=send"),
                         data={
                             "userid":"174",
                             "account":"youzhongyxhy6",
                             "password":"IXh9UT9KyhK8GcAZ0lJv",
                             "mobile":tos,
                             "content":content,
                             "type":"json"
                         },timeout=3,verify=False);
    result = json.loads(resp.content)

###获取post请求内容
class add(tornado.web.RequestHandler):
    def post(self, content=None):
        res = Add(json.loads(self.request.body))
        self.write(json.dumps(res))


def Add(input):
    content = input['content']
    tos = input['tos']
    send_message_example(content, tos);

application = tornado.web.Application([
    (r"/mobile",add)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
