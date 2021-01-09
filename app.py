# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import POSTGRES_URI

APP = Flask('FleetStudio')

APP.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)
MIGRATE = Migrate(APP, DB)


class USERDETAIL(DB.Model):
    __tablename__ = 'USER_DETAILS'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.Text, nullable=False)
    passwd = DB.Column(DB.Text, nullable=False)
    email = DB.Column(DB.Text)
    phone = DB.Column(DB.Numeric)

    def __init__(self, name, passwd, email, phone):
        self.name = name
        self.passwd = passwd
        self.email = email
        self.phone = phone


@APP.route('/')
def hello():
    return jsonify({"status": 200, "result": "Hello World"})

if __name__ == '__main__':
    APP.run(debug=True)
