from flask import Flask, request
from extensions import db,migrate
import importlib
from api.views import blueprint
from extensions import ma
#from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://root:NsINFINITY6617@localhost:3306/db_api' #app.config.get('SQLALCHEMY_DATABASE_URI')
app.register_blueprint(blueprint=blueprint)
db.init_app(app)
migrate.init_app(app,db)
ma.init_app(app)




if __name__ == "__main__":
    app.run(host=app.config.get('host'), port=app.config.get('port'), debug= app.config.get('debug'))
