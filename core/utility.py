

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
