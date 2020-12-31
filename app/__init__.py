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

# The bottom import is a workaround to \
# circular imports, a common problem with Flask applications. 
from app import routes, models
