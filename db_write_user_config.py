from __init__ import db
from models import Material, UserConfig

def userOverride():
    print()
    selectedMaterial = input('Choose the material to change settings for: (PLA / ABS / PETG) ' )

    if selectedMaterial == 'PLA' or selectedMaterial == 'ABS' or selectedMaterial == 'PETG':
        print(f'Now changing configuration for: {selectedMaterial}')

        # Sets up the database to receive input and modify corresponding values
        dbMaterial = Material.query.filter_by(name=selectedMaterial).first()
        materialID = dbMaterial.id

        targetRow = UserConfig.query.filter_by(material_id=materialID).first()

        # Prompts user for input for modified feed rate and target extrusion temperature
        print()
        print(f'Current filament feed rate is {targetRow.feedRate} mm/s')
        userFeedRate = input('New filament feed rate (mm/s): ')
        print(f'New filament feed rate is {userFeedRate} mm/s')
        
        print()
        print(f'Current target temperature is {targetRow.targetTemp} deg C')
        userTargetTemp = input('New target temperature (deg C): ')
        print(f'New target temperature is {userTargetTemp} deg C')

        # Displays the modified values prior to saving so user can confirm changes
        print()
        print('Feed Rate      Target Temperature')
        print(f'{userTargetTemp}            {userFeedRate}')
        saveChanges = input('Save changes? (y/n) ')
        if saveChanges == 'y' or saveChanges == 'Y':
            # Stores user modified values into database
            targetRow.feedRate = userFeedRate
            targetRow.targetTemp = userTargetTemp
            targetRow.minTemp = int(float(userTargetTemp) * 0.95)
            targetRow.maxTemp = int(float(userTargetTemp) * 1.05)
            db.session.commit()
            print('Changes saved successfully!')
            print()

        elif saveChanges == 'n' or saveChanges == 'N':
            # Does not store user modified values into database
            print('Changes will not be saved')
            print()

        else:
            # Prompts user to make a valid choice
            print('Please select (y)es or (n)o to confirm selection')
            userOverride()
    
    else:
        print('Please select an appropriate material')
        userOverride()

if __name__ == '__main__':
    userOverride()