from flask import Flask

from application.config import Config


# add app extensions
# cors, etc


# instantiate, initialize & configure App
# http://flask.pocoo.org/docs/0.12/patterns/appfactories/
def create_app(config_class=Config):

  # CONFIGURATION
  # http://flask.pocoo.org/docs/1.0/config/#configuration-basics
  app = Flask(__name__)
  app.config.from_object(Config)


  # EXTENSIONS
  # bind app to extensions
  # http://flask.pocoo.org/docs/1.0/extensiondev/#the-extension-code


  # REGISTER BLUEPRINTS
  from application.main_routes       import main
  from application.oauth_routes      import oauth

  app.register_blueprint(main)
  app.register_blueprint(oauth)



  return app



