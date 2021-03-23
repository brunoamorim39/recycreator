from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

# Initalize application and connection to database
app = Flask(__name__)

databaseUser = 'root'
databaseEndpoint = 'localhost'
databasePassword = 'password'
databaseSchema = 'recycreator'
DATABASE = f'mysql+pymysql://{databaseUser}:{databasePassword}@{databaseEndpoint}/{databaseSchema}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

# Database Model creation
class Material(db.Model):
    '''
    Model contains list of materials
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    factory_config = db.relationship('FactoryConfig', backref='factory', lazy=True)
    user_config = db.relationship('UserConfig', backref='user', lazy=True)

    def __repr__(self):
        return f'Material: {self.name}, ID: {self.id}'

class FactoryConfig(db.Model):
    '''
    Model contains configuration settings for extrusion of various materials
    '''
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), unique=False, nullable=False)
    feedRate = db.Column(db.String(5), unique=False, nullable=False)
    minTemp = db.Column(db.Integer, unique=False, nullable=False)
    maxTemp = db.Column(db.Integer, unique=False, nullable=False)
    targetTemp = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'Factory Config for {self.material_id}'

class UserConfig(db.Model):
    '''
    Model handles the user-controlled configuration settings for extrusion of varying materials
    '''
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), unique=False, nullable=False)
    feedRate = db.Column(db.String(5), unique=False, nullable=False)
    minTemp = db.Column(db.Integer, unique=False, nullable=False)
    maxTemp = db.Column(db.Integer, unique=False, nullable=False)
    targetTemp = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'User defined Config for {self.material_id}. '

# URL routing to the dashboard where no material information is displayed
@app.route('/')
def dashboard():
    materials = Material.query.all()

    materialArray = []
    for material in materials:
        materialArray.append(material.name)

    return render_template('index.html',
                           materials=materialArray)

# URL routing to page relevant to the material selected, displays temperature data and feed rate for extrusion
@app.route('/<material>')
def pullMaterial(material):
    materials = Material.query.all()
    materialArray = []
    for each in materials:
        materialArray.append(each.name)

    chosenMaterial = Material.query.filter_by(name=material).first()
    selectedMaterial = chosenMaterial.name

    extrusionSettings = UserConfig.query.filter_by(material_id=chosenMaterial.id).first()
    minTemp = extrusionSettings.minTemp
    maxTemp = extrusionSettings.maxTemp
    targetTemp = extrusionSettings.targetTemp
    feedRate = extrusionSettings.feedRate    

    return render_template('index.html',
                           materials=materialArray,
                           selectedMaterial=selectedMaterial,
                           minTemp=minTemp,
                           maxTemp=maxTemp,
                           targetTemp=targetTemp,
                           feedRate=feedRate)
