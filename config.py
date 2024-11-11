import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get('host')
port = os.environ.get('port')
debug = os.environ.get('debug')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
print(host)
print(port)