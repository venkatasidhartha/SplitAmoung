from typing import Union
from django.http import JsonResponse


class CommonResponse:
    message = None
    data = None

    def __init__(self,message:str=None,data:Union[list,dict]=None,status_code:int=200):
        if message != None and message != "":
            self.message = message
        if data != None and (data != {} or data != []):
            self.data = data
        self.status_code = status_code
    

    def get_response(self):
        return JsonResponse({key: value for key, value in vars(self).items() if value is not None},status=self.status_code)
    