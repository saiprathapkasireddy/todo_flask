from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
import os 

file_path = os.path.abspath(os.getcwd())+"/todo.db"

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path 
db = SQLAlchemy(app) 
migrate = Migrate(app, db)


from app import routes 
