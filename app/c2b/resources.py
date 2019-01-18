from flask_restful import Resource, reqparse
from app.utils import get_safaricom_bearer_token
from .utils import APIPARAMS
import requests
from random import randint
import json


def get_random_id():
    return randint(
        11111111111111,
        99999999999999
    )


class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

class CustomerToBusinessRegistration(Resource):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('validation_url', required=True, help='Transaction Validation URL')
        parser.add_argument('confirmation_url', required=True, help='Transaction Confirmation URL')
        parser.add_argument('short_code', required=True, help='Paybill Number')
        parser.add_argument('response_type', required=True, help='Response Type [Completed, Cancelled]')

        args = parser.parse_args()

        try:
            access_token_request = get_safaricom_bearer_token(APIPARAMS.CONSUMER_KEY, APIPARAMS.CONSUMER_SECRET)

            if (not access_token_request):
                return {
                           'error': True,
                           'message': 'unable to get token'
                       }, 400

            access_token = access_token_request['access_token']

            print('access Token is: '+ access_token)

            registration_data = {
                "ShortCode": args['short_code'],
                "ResponseType": args['response_type'],
                "ConfirmationURL": args['confirmation_url'],
                "ValidationURL": args['validation_url']
            }

            custom_headers = {
                "Authorization": "Bearer %s" % access_token
            }

            registration_request = requests.post(
                APIPARAMS.C2B_REGISTRATION_URL_MOCK, json=registration_data, headers=custom_headers
            )

            registration_json = registration_request.json()
            response_code = registration_request.status_code

            print(response_code)

            if (response_code != 200):
                return {
                           'error': True,
                           'request_id': registration_json['requestId'],
                           'error_message': registration_json['errorMessage']
                       }, 400
            else:
                return {
                           'success': True,
                           'registration_status': registration_json['ResponseDescription']
                       }, 200

        except Exception as error:
            print(error)

            return {
                       'success': True,
                       'message': 'Something went wrong! Please try again later'
                   }, 500

class C2BConfirmation(Resource):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('TransactionType', required=False, help='Transaction Type')
        parser.add_argument('TransID', required=False, help='Transaction ID')
        parser.add_argument('TransTime', required=False, help='Transaction Time')
        parser.add_argument('TransAmount', required=False, help='Transaction Amount')
        parser.add_argument('BusinessShortCode', required=False, help='Paybill Number')
        parser.add_argument('BillRefNumber', required=False, help='Account Name')
        parser.add_argument('InvoiceNumber', required=False, help='Invoice Number')
        parser.add_argument('OrgAccountBalance', required=False, help='Account Balance')
        parser.add_argument('ThirdPartyTransID', required=False, help='FD Transaction ID')
        parser.add_argument('MSISDN', required=False, help='Phone Number')
        parser.add_argument('FirstName', required=False, help='Firstname')
        parser.add_argument('MiddleName', required=False, help='Middlename')
        parser.add_argument('LastName', required=False, help='Lastname')

        args = parser.parse_args()

        print('Confirm:', json.dumps(args))

        try:
            kwargs = {
                'transaction_type': args['TransactionType'],
                'transaction_id': args['TransID'],
                'transaction_time': args['TransTime'],
                'transaction_amount': args['TransAmount'],
                'business_short_code': args['BusinessShortCode'],
                'account_name': args['BillRefNumber'],
                'invoice_number': args['InvoiceNumber'],
                'organization_account_balance': args['OrgAccountBalance'],
                'phone_number': args['MSISDN'],
                'firstname': args['FirstName'],
                'middlename': args['MiddleName'],
                'lastname': args['LastName'],
                'trans_processed': 0
            }

            return {
                       'ResultCode': 0,
                       'ResultDesc': 'Success',
                       'ThirdPartyTransID': get_random_id()
                   }, 200

        except Exception as error:

            return {
                       'ResultCode': 500,
                       'ResultDesc': 'Something went wrong! Please try again later',
                       'ThirdPartyTransID': get_random_id()
                   }, 200


class C2BValidation(Resource):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get(self):
        pass

    def post(self):
        return {
                   'ResultCode': 0,
                   'ResultDesc': 'Success',
                   'ThirdPartyTransID': get_random_id()
               }, 200