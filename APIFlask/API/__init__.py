from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config') # Confirmando o modo de debug 

db = SQLAlchemy(app)
ma = Marshmallow(app)
Migrate = Migrate(app, db)
api = Api(app)