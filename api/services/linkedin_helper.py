from django.conf import settings
import requests

BASE_URL = 'https://www.linkedin.com'
API_BASE_URL = 'https://api.linkedin.com'

def get_access_token(authorization_code):
    grant_type = 'authorization_code'
    body = {
        'grant_type': grant_type,
        'code': authorization_code,
        'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
        'client_id': settings.LINKEDIN_CLIENT_ID,
        'client_secret': settings.LINKEDIN_CLIENT_SECRET
    }
    url = BASE_URL + "/oauth/v2/accessToken"

    response = requests.post(url, data=body, verify=False)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response_json = response.json()
        return None, response_json

    decoded_response = response.json()
    access_token = decoded_response['access_token']
    expires_in = decoded_response['expires_in']
    return access_token, expires_in

def get_profile_data(user_token):
    profile_data_to_request = "firstName,lastName,summary,profilePicture"
    request = f'/v2/people/me?projection=({profile_data_to_request})'
    url = API_BASE_URL + request
    authorization_header = 'Bearer ' + user_token
    headers = {'Authorization': authorization_header}

    response = requests.get(url, headers=headers, verify=False)

    try:
        response.raise_for_status()
        decoded_response = response.json()
        return decoded_response
    except requests.exceptions.HTTPError as e:
        response_json = response.json()
        return None, response_json['error_description']
