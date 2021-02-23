from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initalize application and connection to database
app = Flask(__name__)

DATABASE = 'sqlite:///recycreator.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

db = SQLAlchemy(app)

# Database Model creation
class Material(db.Model):
    '''
    Model contains list of materials
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    extrusion = db.relationship('ExtrusionConfig', backref='extrusion', lazy=True)

class ExtrusionConfig(db.Model):
    '''
    Model contains configuration settings for extrusion of various materials
    '''
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.String(30), db.ForeignKey('material.id'), unique=False, nullable=False)
    feedRate = db.Column(db.Integer, unique=False, nullable=False)
    minTemp = db.Column(db.Integer, unique=False, nullable=False)
    maxTemp = db.Column(db.Integer, unique=False, nullable=False)
    targetTemp = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<ExtrusionConfig %r>' %self.material

@app.route('/')
def dashboard():
    materials = Material.query.all()

    materialArray = []
    for material in materials:
        materialArray.append(material.name)

    extrusionSettings = ExtrusionConfig.query.filter_by(material_id=1).first()

    minTemp = extrusionSettings.minTemp
    maxTemp = extrusionSettings.maxTemp
    targetTemp = extrusionSettings.targetTemp

    return render_template('index.html', materials=materialArray, minTemp=minTemp, maxTemp=maxTemp, targetTemp=targetTemp)