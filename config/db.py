import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)
api = Api(app)


#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'

#disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True
# mysql db connect

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$Cambodia__089$@localhost:3306/dbpartychecklist'
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://b87f2af3c7a476:c9fa25c8@us-cdbr-east-06.cleardb.net/heroku_ff795760167803c'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CLEARDB_DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True

db = SQLAlchemy(app)



# app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
# app.config["JWT_HEADER_NAME"] = "JWT"
# app.config["JWT_HEADER_TYPE"] = "Bearer"

# app.config["JWT_BLACKLIST_ENABLED "] = True

# app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
# app.config["JWT_COOKIE_SECURE"] = False

