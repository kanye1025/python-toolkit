import hashlib


def md5(str,lenth = None):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    if not lenth:
        return m.hexdigest()
    else :
        return m.hexdigest()[:lenth]


if __name__ == "__main__":
    print(md5('你好',15))