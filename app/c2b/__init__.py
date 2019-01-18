from flask_restful import Api
from flask import Blueprint
from . import resources as c2b_resource

c2b = Blueprint('c2b', __name__)

api = Api(c2b)

api.add_resource(c2b_resource.Hello,'/', endpoint='/Hello')

api.add_resource(c2b_resource.CustomerToBusinessRegistration, '/laas/register', endpoint='/laas/repayment_register',
                 methods=['POST'])
api.add_resource(c2b_resource.C2BConfirmation, '/laas/confirmation', endpoint='/laas/repayment_result',
                 methods=['POST', 'GET'])
api.add_resource(c2b_resource.C2BValidation, '/laas/validation', endpoint='/lass/repayment_validate',
                 methods=['POST', 'GET'])