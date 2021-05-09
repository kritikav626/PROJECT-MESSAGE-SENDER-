'''---IT'S A PROJECT ON MESSAGE_SENDER  WHICH HELPS YOU TO RECIEVE OTP'S SMS FROM  PEOPLE...'''
import requests
import json

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    params = {
        'authorization': '9MIPR2LUzOIvBZwlcTG4dPCHtUhW1VQcTemwySo1JhebjhCbYaKppCqsTgQ6',
        'sender_id': "FSTSMS",
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


send_sms("7836912682","hi this is kritika")