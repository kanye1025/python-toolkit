import requests
import json
import traceback
class GPT:
    def __init__(self,url,sk,model):
        self.h = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {sk}'
                }

        self.u =  f'{url}/v1/completions'
        self.model = model


    def predict(self,text,**kwargs):
        d = {
            "model":self.model,
            "prompt": text,
            "max_tokens": 4096,
            "temperature": 0,
        }
        d.update(kwargs)
        r = requests.post(url=self.u, headers=self.h, json=d, verify=False).json()
        if 'error' in r :
            raise Exception(r['error']['code'])
        if 'choices' in r:
            return r['choices'][0]['text']


    def predict_json(self,text,**kwargs):
        text = "问:"+text+"\n答:好的，返回json数据为```{"
        res = self.predict(text,stop = ["```"],**kwargs)
        res = "{"+res
        try:
            ret = json.loads(res)
            return ret
        except Exception as e :
            print(f"gpt error :{text}")
            raise e

    def predict_json2(self,text,**kwargs):

        res = self.predict(text,**kwargs)
        #print(res)
        try:
            ret = json.loads(res)
            return ret
        except Exception as e :
            print(f"gpt error :{text}")
            print(res)
            raise e
