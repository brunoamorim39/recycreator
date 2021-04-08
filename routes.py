from flask import render_template

from models import Material, UserConfig
from __init__ import app

# URL routing to the dashboard where no material information is displayed
@app.route('/')
def dashboard():
    materials = Material.query.all()

    materialArray = []
    for material in materials:
        materialArray.append(material.name)

    return render_template(
        'index.html',
        materials=materialArray
        )

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

    return render_template(
        'index.html',
        materials=materialArray,
        selectedMaterial=selectedMaterial,
        minTemp=minTemp,
        maxTemp=maxTemp,
        targetTemp=targetTemp,
        feedRate=feedRate
        )
