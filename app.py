from flask import *
from flask import session as login_session
from model import *
from database import *

app = Flask(__name__)

@app.route('/')
def homepage():
    a=login_session['FirstName']
    return render_template("home.html",a=a)

@app.route('/signup',methods=['GET','POST'])
def signUp():
    if request.method == 'POST':
        firstName=request.form['fname']
        lastName=request.form['lname']
        age=request.form['age']
        gender=request.form['gender']
        email=request.form['email']
        password=request.form['password']
        AddStudent(firstName,lastName,age,gender,email,password)
        return redirect(url_for('homepage'))
    else:
        return render_template("signup.html")

@app.route('/teachersignup',methods=['GET','POST'])
def teacherSignUp():
    if request.method == 'POST':
        firstName=request.form['fname']
        lastName=request.form['lname']
        age=request.form['age']
        gender=request.form['gender']
        email=request.form['email']
        password=request.form['password']
        subject=request.form['subject']
        yearsOfExp=request.form['expyears']
        available=True
        AddTeacher(firstName,lastName,age,gender,email,password,subject,yearsOfExp,available)
        return redirect(url_for('homepage'))
    return render_template("teachersignup.html")

@app.route('/login',methods=['GET','POST'])
def login():
    txt=""
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        student = GetStudentByEmail(email)
        return redirect(url_for('homepage'))
    else:
        return render_template("login.html")

if __name__ == '__main__':
   app.run(debug = True)

