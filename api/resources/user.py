from flask import request,jsonify
from flask_restful import Resource, abort
from models.users import users
from extensions import db
from schema.forum import UserSchema


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
        schema = UserSchema(many=True)
        return {'result':schema.dump(user)}
    
    def post(self):
        schema = UserSchema()
        validated_data = schema.load(request.json)
        new_user = users(**validated_data)
        db.session.add(new_user)
        db.session.commit()
        return {'msg':'new user is successful', 'user':schema.dump(new_user)}
class UserResource(Resource):
    def get(self,user_id):
        schema = UserSchema()

        user = users.query.get_or_404(user_id)


        return {'result':schema.dump(user)}

    def put(self, user_id):
        
        schema = UserSchema(partial=True,)
        # partial is used because we are not returning all the fields, just only name and age
        user = users.query.get_or_404(user_id)
        user = schema.load(request.json, instance=user)

        db.session.add(user)
        db.session.commit()
        return {'msg':'user Updated','result':schema.dump(user)}
    

    def delete(self,user_id):
        user = users.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()
        return {'msg':'user successfully removed'}
