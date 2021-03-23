from app import db, Material, FactoryConfig, UserConfig

# Initialize MySQL database
materials = ['PLA', 'ABS', 'PETG']
materialIDs = [1, 2, 3]
feedRates = [0.2, 0.25, 0.18]
minTemps = [230, 250, 220]
maxTemps = [270, 280, 260]
recTemps = [245, 260, 240]

db.create_all()

for i in range(len(materials)):
    db.session.add(Material(name=materials[i]))
    db.session.add(FactoryConfig(
        material_id=materialIDs[i], 
        feedRate=feedRates[i], 
        minTemp=minTemps[i], 
        maxTemp=maxTemps[i], 
        targetTemp=recTemps[i]
        ))
    db.session.add(UserConfig(
        material_id=materialIDs[i], 
        feedRate=feedRates[i], 
        minTemp=minTemps[i], 
        maxTemp=maxTemps[i], 
        targetTemp=recTemps[i]
        ))
    db.session.commit()