from __init__ import db
from models import Material, FactoryConfig, UserConfig

def factoryReset():
    print()
    matSelect = input('Which material settings do you want to restore? (PLA / ABS / PETG) ')

    if matSelect == 'PLA' or matSelect == 'ABS' or matSelect == 'PETG':
        confirm = input('Are you sure you want to restore default settings? (y/n) ')
        if confirm == 'y' or confirm == 'Y':
            print('Restoring default settings...')
            
            # Query database to find the default values that will be applied to the selected material
            mat = Material.query.filter_by(name=matSelect).first()
            matID = mat.id

            defaultSettings = FactoryConfig.query.filter_by(material_id=matID).first()
            targetRow = UserConfig.query.filter_by(material_id=matID).first()

            # Updates the values for the selected row witht the material information
            targetRow.material_id = defaultSettings.material_id,
            targetRow.feedRate = defaultSettings.feedRate
            targetRow.minTemp = defaultSettings.minTemp
            targetRow.maxTemp = defaultSettings.maxTemp
            targetRow.targetTemp = defaultSettings.targetTemp

            db.session.commit()
            print('Default settings restored successfully')
            print()
            
        elif confirm == 'n' or confirm == 'N':
            # Does not store user modified values into database
            print('Default settings will not be restored')
            print()

        else:
            # Prompts user to make a valid choice
            print('Please select (y)es or (n)o to confirm selection')
            factoryReset()

    else:
        print('Please select the appropriate material to restore')
        factoryReset()

if __name__ == '__main__':
    factoryReset()