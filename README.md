The intent for this project is to allow for the host device to run its own locally hosted web server, which it then uses to communicate between itself and a locally hosted MySQL database. This channel of communication allows for certain functions, such as the restoration of factory settings, as well as the overriding of settings by the user, to exist.

- app.py: Host of the locally hosted web server, stores definitions of databse models and serves as the channel of communication between other scripts and the MySQL database
- db_init.py: Runs only once during pre-shipment setup. Sole purpose is to initialize the MySQL database with material ID's as well as factory and user configuration tables
- db_restore_factory_config.py: Used only when the objective is to return extrusion parameters back to the values assigned prior to shipment
- db_write_user_config.py: Used in order to redefine configuration values for extrusion. The user is able to change these values in order to suit their personal use cases