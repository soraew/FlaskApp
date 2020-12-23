from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy# wrapper for SQLAlchemy
from flask_migrate import Migrate# for db migration (useful for making db changes)

app = Flask(__name__)

#config variables
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models
# The bottom import is a workaround to \
# circular imports, a common problem with Flask applications. 

