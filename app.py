from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "Thisissupposedtobesecret"

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])
    remember = BooleanField('remember me')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)