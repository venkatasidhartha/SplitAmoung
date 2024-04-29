from typing import Union

class Response:
    message = "success"
    status_code = 200
    data = None

    def __init__(self,message:str=None,status_code:int=None,data:Union[dict,list]=None):
        if message != None:
            self.message = message
        if status_code != None:
            self.status_code = status_code
        if data != None:
            self.data = data
    
    def __call__(self):
        return {attr: getattr(self, attr) for attr in dir(self) if not attr.startswith('__') and getattr(self, attr) not in (None, "")}

