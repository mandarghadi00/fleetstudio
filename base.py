# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_URI

engine = create_engine(POSTGRES_URI)
Session = sessionmaker(bind=engine)
