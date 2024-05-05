

class ProfileResponse:
    email = None
    name = None
    phone = None
    message = None
    s3_url = None
    s3_id = None

    def get_dict(self):
        return {key: value for key, value in vars(self).items() if value is not None}

    def set_email(self,email):
        self.email = email
    def set_name(self,name):
        self.name = name
    def set_phone(self,phone):
        self.phone = phone
    def set_message(self,message):
        self.message = message
    def set_s3_url(self,s3_url):
        self.s3_url = s3_url
    def set_s3_id(self,s3_id):
        self.s3_id = s3_id