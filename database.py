from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///accounts.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def AddStudent(firstName,lastName,age,gender,email,password):
    st=Student(FirstName=firstName,LastName=lastName,Age=age,Gender=gender,Email=email,Password=password)
    session.add(st)
    session.commit()

def AddTeacher(firstName,lastName,age,gender,email,password,subject,yearsOfExperience,available):
    t=Teacher(FirstName=firstName,LastName=lastName,Age=age,Gender=gender,Email=email,Password=password,Subject=subject,YearsOfExperience=yearsOfExperience,Available=available)
    session.add(t)
    session.commit()

def GetStudentByEmail(email):
    stud=session.query(Student).filter_by(Email=email).first()
    return stud

def GetTeacherByEmail(email):
    t=session.query(Teacher).filter_by(Email=email).first()
    return t

def AddArticle(title,content,name,email):
    a=Article(Title=title,Content=content,Publisher=name,Email=email)
    session.add(a)
    session.commit()

def GetAllArticles():
    a=session.query(Article).all()
    articles = []
    articles = a
    return articles