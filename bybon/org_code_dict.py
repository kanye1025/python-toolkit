import pandas as pd
from collections import defaultdict

class OrgCodeDict:
    def __init__(self,file_path):
        df = pd.read_csv(file_path,dtype = {"customer_code":str,"store_code":str})
        d_to_customer = defaultdict(dict)
        d_from_customer =defaultdict(dict)
        for customer_code,store_code,sys_type in zip(df['customer_code'],df['store_code'],df['sys_type']):
            if pd.isna(customer_code) or pd.isna(store_code):
                continue
            d_to_customer[sys_type][store_code]=customer_code
            d_from_customer[sys_type][customer_code]=store_code

        self.d_to_customer = d_to_customer
        self.d_from_customer = d_from_customer


    def to_customer(self,sys,code):
        return self.d_to_customer[sys].get(code,None)


    def from_customer(self,sys,code):
        return self.d_from_customer[sys].get(code,None)





