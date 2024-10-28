from flask import request,jsonify
from flask_restful import Resource, abort
from model import users
from extensions import db



'''class UserList(Resource):
    def get(self):

        return jsonify(users)
    

    def post(self):
        user = None
        data = request.json
        last_row_id = users[-1][id] 
        user = {"id":last_row_id + 1, **data}
        try:
            users.append(user)
            return {'msg':'user created', 'user':user}
        except:
            return abort(404)
        


class UserResource(Resource):
    def get(self,user_id):
        user = next(filter(lambda u: u.get('id') == user_id, users),None)
        if user is None :
            return abort(404)
        else:
            return {'result':user}

    def put(self,user_id):
        user = None
        data = request.json
        for i,u in enumerate(users):
            if u[id] == user_id:
                users[i] = {**user,**data}
                user = users[i]
                if user is None:
                    return abort(404)
                else:
                    return {'msg':'user created', 'result':user}
    def delete(self, user_id):
        user = None
        for i,u in enumerate(users):
            if u[id] == user_id:
                user = users[i]
                users.pop(user)
                return {'msg':'user is deleted', 'user':user}
            else:
                abort(404)'''
class UserList(Resource):
    def get(self):
        user = users.query.all()
        return jsonify(user)
    
    def post(self):
        data = request.json
        new_user = users(
            name = data.name,
            email = data.email,
            age = data.age,
        )
        db.session.add(new_user)
        db.session.commit()
        return {'msg':'new user is successful', 'user':new_user}
class UserResource(Resource):
    pass

