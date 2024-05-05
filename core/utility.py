import traceback
from django.http import JsonResponse
from django.conf import settings

def extract_username_from_email(email):
    """
    Extracts the username from an email address.
    
    Args:
        email (str): The email address from which to extract the username.
    
    Returns:
        str: The extracted username.
    """
    username = email.split('@')[0]
    return username


def capture_error(function):
    def executor(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(e.__str__())
            response = {
                "error":e.__str__(),
                "message":"failed",
                "status_code":500
            }
            if settings.DEBUG:
                response["exception"] = traceback.format_exc()
            return JsonResponse(response,status=500,safe=False)
    return executor

def extract_file_extenstion(filename):
    extrnstion = filename.split(".")[-1]
    return extrnstion