from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy# wrapper for SQLAlchemy
from flask_migrate import Migrate# for db migration (useful for making db changes)
from flask_login import LoginManager

app = Flask(__name__)

#config variables
app.config.from_object(Config)

#set db and migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

login = LoginManager(app)
login.login_view = 'login'# The 'login' value above is the function \
                          # (or endpoint) name for the login view. \
                          # In other words, the name you would use in a url_for() call to get the URL.

# The bottom import is a workaround to \
# circular imports, a common problem with Flask applications. 
from app import routes, models
