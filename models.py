from __init__ import db

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
    Model contains configuration settings for extrusion of various materials predetermined and set from the factory
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