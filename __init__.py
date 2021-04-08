from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')

databaseUser = 'root'
databaseEndpoint = 'localhost'
databasePassword = 'password'
databaseSchema = 'recycreator'
DATABASE = f'mysql+pymysql://{databaseUser}:{databasePassword}@{databaseEndpoint}/{databaseSchema}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)