class Error(Exception):
    def __init__(self,code,msg = ""):
        self.code = code
        self.msg = msg
        super(Error, self).__init__(f"error code {code}:{msg}")