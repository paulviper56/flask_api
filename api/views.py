from flask import Blueprint,jsonify
#import importlib
from flask_restful import Api
from .resources.user import UserList, UserResource
from marshmallow import ValidationError

#for_userlist = importlib.import_module('api.resources.user')
#my_func = getattr(for_userlist,'UserList')

blueprint= Blueprint("api", __name__ , url_prefix ="/api")

api = Api(blueprint, errors=blueprint.errorhandler)
api.add_resource(UserList, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages),400

