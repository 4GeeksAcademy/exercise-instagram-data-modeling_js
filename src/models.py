import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Define columns for the table user
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    profile_image = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    # Define columns for the table post
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    caption = Column(String(2200))
    image_url = Column(String(250))
    created_at = Column(String(100))

class Comment(Base):
    __tablename__ = 'comment'
    # Define columns for the table comment
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    text = Column(String(500))
    created_at = Column(String(100))

class Like(Base):
    __tablename__ = 'like'
    # Define columns for the table like
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    created_at = Column(String(100))

## Generate the ER diagram
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
