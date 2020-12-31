from flask import render_template, flash, redirect, url_for
# flash is for flash elements
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required


@app.route('/')
@app.route('/index')
# This means that when a web browser requests either of these two URLs('/'or'/index'), \
# Flask is going to invoke this function \
# and pass the return value of it back to the browser as a response. 
@login_required
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

# Login
@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:# current_user is a flask_login variable
        return redirect(url_for('index'))# so that a unknown user doesn't login
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))# generating urls instead of hard coding 
                                             # is better for updating reasons
        login_user(user, remember=form.remember_me.data)# login_user also comes from flask_login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

#Logout       
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



    

    