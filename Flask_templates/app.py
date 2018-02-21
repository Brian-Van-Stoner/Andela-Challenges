from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from data import Business
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

Business = Business()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/business')
def business():
    return render_template('business.html', business = Business)

@app.route('/businesses/<string:id>')
def businesses(id):
    return render_template('businesses.html', id=id)

@app.route('/about')
def about():
    return render_template('about.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email= StringField('Email', [validators.Length(min=9, max=50)])
    password= PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('Confirm', message='Password has no match')
    ])
    confirm = PasswordField('Confirm Password')

#@app.route('/register', methods=['GET', 'POST'])
#def register():
#    form = RegisterForm(request.form)
#    if request.method == 'POST' and form.validate();

#    return

# This line means that your flask app will being run if we run from app.py
if __name__ == '__main__':
    app.run(debug=True) 
