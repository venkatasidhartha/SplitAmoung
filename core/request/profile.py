

class ProfileRequest:
    email = None
    name = None
    phone = None

    def __init__(self,data) -> None:
        if "email" not in data:
            raise Exception("email is missing")
        self.email = data["email"]
        if "name" in data:
            self.name = data["name"]
        if "phone" in data:
            self.phone = data["phone"]
    
    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    