# coding: utf-8
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

from sqlalchemy import Column, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserDetail(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_details_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    passwd = Column(Text, nullable=False)
    email = Column(Text)
    phone = Column(Text)
    
    def __init__(self, name, passwd, email, phone):
        self.name = name
        self.passwd = passwd
        self.email = email
        self.phone = phone