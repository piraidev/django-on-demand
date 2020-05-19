import sendgrid
import os
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Personalization
from django.conf import settings
import requests

def send_email(to_email, template_id, dynamic_template_data):
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_CLIENT_KEY)
    mail = Mail()
    mail.template_id = template_id
    mail.from_email = Email(settings.FROM_EMAIL_ADDRESS, settings.FROM_NAME)
    p = Personalization()
    p.add_to(Email(to_email))
    p.dynamic_template_data = dynamic_template_data
    mail.add_personalization(p)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code < 300:
            print("Email #{} processed".format(template_id), response.body, response.status_code)
    except requests.exceptions.HTTPError as e:
        raise Exception("")

def unsubscribe_user(user_email):
    print('Unsubscribing user ', user_email)
    url = 'https://api.sendgrid.com/v3/asm/suppressions/global'
    body = '{"recipient_emails":["' + user_email + '"]}'
    token = f'Bearer {settings.SENDGRID_API_CLIENT_KEY}'
    headers = {'authorization': token}
    try:
        response = requests.post(url, data=body, headers=headers)
        decoded_response = response.json()
        if('errors' in decoded_response and len(decoded_response['errors']) > 0):
            raise Exception("")
        print('Successfully unsubscribed user ', user_email)
        return response
    except requests.exceptions.HTTPError as e:
        raise Exception("")

def subscribe_user(user_email):
    print('Subscribing user ', user_email)
    url = f'https://api.sendgrid.com/v3/asm/suppressions/global/{user_email}'
    token = f'Bearer {settings.SENDGRID_API_CLIENT_KEY}'
    headers = {'authorization': token}
    try:
        response = requests.delete(url, headers=headers)
        if(response.status_code == 204):
            return response
        else:
            raise Exception("")
    except requests.exceptions.HTTPError as e:
        raise Exception("")

def user_is_subscribed(user_email):
    url = f'https://api.sendgrid.com/v3/asm/suppressions/global/{user_email}'
    token = f'Bearer {settings.SENDGRID_API_CLIENT_KEY}'
    headers = {'authorization': token}
    try:
        response = requests.get(url, headers=headers)
        decoded_response = response.json()
        if('errors' in decoded_response and len(decoded_response['errors']) > 0):
            raise Exception("")
        if('recipient_email' in decoded_response and decoded_response['recipient_email'] == user_email):
            return False
        return True
    except requests.exceptions.HTTPError as e:
        raise Exception("")