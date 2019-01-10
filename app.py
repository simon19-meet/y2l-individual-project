from flask import *
from flask import render_template
from model import *
from databases import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/signup')
def signUp():
    return render_template("signup.html")

@app.route('/teachersignup')
def teacherSignUp():
    return render_template("teachersignup.html")

if __name__ == '__main__':
   app.run(debug = True)

