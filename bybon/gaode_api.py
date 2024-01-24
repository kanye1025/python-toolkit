
import requests
key ="b17f6920dc6176446f9c9c1b0280a3c2"



def get_coordinate(address,city= None):
    """
    :param address:
    :param city:
    :return:longitude,latitude
    """
    url = "https://restapi.amap.com/v3/geocode/geo"
    myParams = {"city": city, 'address': address,"key":key}  if city else  { 'address': address,"key":key}
    res = requests.get(url=url, params=myParams)
    res =res.json()
    if res['status'] and res['status']!='0':
        print(address,res['geocodes'][0]['location'])
        return res['geocodes'][0]['location'].split(',')
    else:
        print(Exception(res["info"]))
        return "",""
        #raise Exception(res["info"])



def get_address(longitude,latitude):
    url = "https://restapi.amap.com/v3/geocode/regeo"
    myParams = {"location": f"{longitude},{latitude}",'extensions': "base", "key": key}
    res = requests.get(url=url, params=myParams)
    res = res.json()
    if res['status']:
        return res['regeocode']['formatted_address']
    else:
        raise Exception(res["info"])
if __name__ == '__main__':

    print(get_coordinate("沧州 新华中路80号智慧广场联通大厦B座"))
    #print(get_address(121.295417325, 31.1983962))
    #print(get_address(121.57377827500001, 31.07814915))
    #print(get_address(121.613544125, 31.164039900000002))
