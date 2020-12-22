from flask import Flask
from config import Config

app = Flask(__name__)

#config variables
app.config.from_object(Config)


from app import routes
# The bottom import is a workaround to \
# circular imports, a common problem with Flask applications. 

