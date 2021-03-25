from app import db, Material, FactoryConfig, UserConfig

def interactionMenu():
    matSelect = input('Which material settings do you want to restore? [PLA / ABS / PETG] ')

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
            print('Default settings restored')
            
        elif confirm == 'n':
            print('Default settings will not be restored')

        else:
            print('Please select y or n to confirm selection')
            interactionMenu()

    else:
        print('Please select the appropriate material to restore')
        interactionMenu()

if __name__ == '__main__':
    interactionMenu()