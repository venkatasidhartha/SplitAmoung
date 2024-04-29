

class Request:
    email = None
    name = None
    phone = None

    def __init__(self,request) -> None:
        if "email" not in request:
            raise Exception("email is missing")
        self.email = request["email"]
        if "name" in request:
            self.name = request["name"]
        if "phone" in request:
            self.phone = request["phone"]
    
    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    