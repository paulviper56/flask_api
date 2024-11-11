from extensions import ma
from models.users import users
from marshmallow.fields import String
from marshmallow import validate,validates_schema
from marshmallow import ValidationError

 

class UserSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True, validate=[validate.Length(min=3)])
    email = String(required=False, validate=[validate.Email()])


    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get('email')

        if users.query.filter_by(email=email).count() :
            raise ValidationError(f"email:{email} already exist")
        # to check for email; if the email already exist



    class Meta:
        model = users
        load_instance = True
        exclude = ['id']

    

