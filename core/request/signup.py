

class SignupRequest:
    email = None
    password = None

    def __init__(self,data):
        if "email" not in data or data["email"] == "":
            raise Exception("email is missing")
        if "password" not in data or data["password"] == "":
            raise Exception("password is missing")
        self.email = data["email"]
        self.password = data["password"]

    def get_email(self):
        return self.email 
    def get_password(self):
        return self.password