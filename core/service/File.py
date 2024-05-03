

class FileService:
    """
    This service is to handel File model and S3 object storage
    """
    def upload(self,user_id:int=None,table_name:str=None,table_field:str=None,file=None):
        if user_id == None or user_id == "":
            raise Exception("user_id is required")
        if table_name == None or table_name == "":
            raise Exception("table_name is required")
        if table_field == None or table_field == "":
            raise Exception("table_field is required")
        if table_field == None or table_field == "":
            raise Exception("table_field is required")
        if file == None or file == "":
            raise Exception("file is required")
        