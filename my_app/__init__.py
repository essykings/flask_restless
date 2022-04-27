import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

from my_app.product.views import catalog

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
# api = Api(app)


app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


manager = APIManager(app, flask_sqlalchemy_db=db)

app.register_blueprint(catalog)
 
db.create_all()