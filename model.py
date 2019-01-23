from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    FirstName= Column(String)
    LastName= Column(String)
    Age= Column(Integer)
    Gender= Column(String)
    Email=Column(String)
    Password=Column(String)

class Teacher(Base):
    __tablename__="teachers"
    id=Column(Integer,primary_key=True)
    FirstName= Column(String)
    LastName= Column(String)
    Age= Column(Integer)
    Gender= Column(String)
    Email=Column(String)
    Password=Column(String)
    Subject= Column(String)
    YearsOfExperience=Column(Integer)
    Available=Column(Boolean)

class Article(Base):
    __tablename__="articles"
    id=Column(Integer,primary_key=True)
    Title=Column(String)
    Content=Column(String)
    Publisher=Column(String)
    Email=Column(String)
    