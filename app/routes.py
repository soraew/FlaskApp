from flask import render_template, flash, redirect, url_for
# flash is for flash elements
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
# @app.route('/dic')

# This means that when a web browser requests either of these two URLs, \
# Flask is going to invoke this function \
# and pass the return value of it back to the browser as a response. 

def index():
    user = {'username': 'Alyosha'}
    posts = [
        {
            'author':{'username':'Ivankov'},
            'body':'I did not kill my father'
        },
        {
            'author':{'username':'Simachev'},
            'body':'I saw him kill his father'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


# -for rendering, you only need to import a class and create a object
#   and pass it to the render_template method
# -the default method is only GET
# -POST requests are typically used when the browser submits form data
#   to the server
# -by providing the methods argument, 
#   you are telling Flask which request methods should be accepted.
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}"\
            .format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
    
    