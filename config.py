import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get('host')
port = os.environ.get('port')
print(host)
print(port)