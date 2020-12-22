from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired#makes sure the field is not submitted empty
# validators attaches validation behaiviors to fields.

# The Flask-WTF extension uses Python classes to represent web forms.
# A form class simply defines the fields of the form as class variables.
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")#checkbox
    submit = SubmitField("Sign In")
    
    