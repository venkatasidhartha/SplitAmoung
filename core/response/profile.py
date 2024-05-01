

class ProfileResponse:
    email = None
    name = None
    phone = None

    def get_dict(self):
        return {key: value for key, value in vars(self).items() if value is not None}

    def set_email(self,email):
        self.email = email
    def set_name(self,name):
        self.name = name
    def set_phone(self,phone):
        self.phone = phone