from __init__ import db
from models import Material, FactoryConfig, UserConfig

materials = []
materialIDs = []
feedRates = []
minTemps = []
maxTemps = []
recTemps = []

def defaults():
    # Initialize MySQL database factory values
    materials = ['PLA', 'ABS', 'PETG']
    materialIDs = [1, 2, 3]
    feedRates = [0.2, 0.25, 0.18]
    minTemps = [230, 250, 220]
    maxTemps = [270, 280, 260]
    recTemps = [245, 260, 240]

    return materials, materialIDs, feedRates, minTemps, maxTemps, recTemps

def firstRun(materials, materialIDs, feedRates, minTemps, maxTemps, recTemps): 
    # Generate the database tables described in app.py
    db.create_all()

    # Iterate over factory config lists and add+commit to database session
    for i in range(len(materials)):
        db.session.add(Material(name=materials[i]))
        writeValues(FactoryConfig,
            materialIDs[i],
            feedRates[i],
            minTemps[i],
            maxTemps[i],
            recTemps[i]
            )
        writeValues(UserConfig,
            materialIDs[i],
            feedRates[i],
            minTemps[i],
            maxTemps[i],
            recTemps[i]
            )
    print()
    print('Database successfully initialized')
    print()

# Handles writing and commitment of values to the specified table
def writeValues(table, id, feed, minT, maxT, recT):
    db.session.add(table(
        material_id = id,
        feedRate = feed,
        minTemp = minT,
        maxTemp = maxT,
        targetTemp = recT
    ))
    db.session.commit()

if __name__ == '__main__':
    mats, IDs, feedRates, minTs, maxTs, recTs = defaults()
    firstRun(mats, IDs, feedRates, minTs, maxTs, recTs)