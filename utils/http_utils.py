import os
from urllib.parse import urljoin
import json
import requests
from toolkit.utils.error import Error
class HttpCall:
    def __init__(self):
        raise "HttpCall is a base class ,please use a derived class"
        pass
    def __call__(self, *args, **kwargs):
        raise "HttpCall is a base class ,please use a derived class"
        pass

class JsonHttpCall(HttpCall):
    def __init__(self,root_url):
        self.root_url = root_url
        self.headers =  {"content-type": "application/json"}
    def __call__(self, func_name,request_type = 'POST',**param):
        url = urljoin(self.root_url, func_name)
        #call = getattr(requests,request_type)
        res = requests.request(request_type,url = url,json=param,headers=self.headers)
        #res = call(url, json=param, headers=self.headers)
        try:
            ret = json.loads(res.text)
            return ret
        except Exception as e:
            raise Error(code=-1,msg=str(e))

