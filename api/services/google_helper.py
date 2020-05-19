import json
import requests

def debug_token(token):
    url = f'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token}'
    response = requests.post(url, verify=False)
    return response

def is_valid_token(request_data):
    token = request_data['token']
    email = request_data['email']

    try:
        response = debug_token(token)
        response.raise_for_status()
        decoded_response = response.json()
        is_valid = decoded_response['email_verified']
        if(is_valid and (email == decoded_response['email'])):
            return True, decoded_response['exp']
        return False, 'Wrong credentials'
    except requests.exceptions.HTTPError as e:
        response_json = response.json()
        return False, response_json