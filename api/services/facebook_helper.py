from django.conf import settings
import requests
import json

def debug_token(token):
    url = f'https://graph.facebook.com/debug_token?input_token={token}&access_token={settings.FACEBOOK_ACCESS_TOKEN}'
    response = requests.get(url)
    return response

def provided_data_is_consistent(provided_user_id, token_user_id, email):
    return email and (provided_user_id == token_user_id)

def is_valid_token(request_data):
    token = request_data['token']
    email = request_data['email']
    provided_user_id = request_data['user_id']
    try:
        response = debug_token(token)
        response.raise_for_status()
        decoded_response_data = response.json()['data']
        is_valid = decoded_response_data['is_valid']
        if is_valid and provided_data_is_consistent(provided_user_id, decoded_response_data['user_id'], email):
            return True, decoded_response_data['expires_at']
        return False, 'Wrong credentials'
    except requests.exceptions.HTTPError as e:
        response_json = response.json()
        return False, response_json