from flask import Flask, render_template, request, flash, redirect, url_for, session, logging

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True) 
