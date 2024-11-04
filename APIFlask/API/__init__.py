from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config') # Confirmando o modo de debug 

db = SQLAlchemy(app)
Migrate = Migrate(app, db)
api = Api(app)