import requests


def get_safaricom_bearer_token(consumer_key, consumer_secret):
    try:
        token_request = requests.get('https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
                                     auth=(consumer_key, consumer_secret), headers={'Accept': 'application/json'})
        response_code = token_request.status_code

        if response_code != 200:
            return False
        else:
            return token_request.json()
    except Exception as error:
        return False