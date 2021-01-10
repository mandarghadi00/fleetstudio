# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

import os
from datetime import timedelta
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_expects_json import expects_json
from config import POSTGRES_URI, SIGNUP_SCHEMA

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
    phone = DB.Column(DB.Text)

    def __init__(self, name, passwd, email, phone):
        self.name = name
        self.passwd = passwd
        self.email = email
        self.phone = phone


@APP.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username'].upper()
        password = data['password']
        user = USERDETAIL.query.filter_by(name=username, passwd=password).first()
        if user:
            session["logged"] = True
            session.permanent = True
            APP.permanent_session_lifetime = timedelta(minutes=5)
            return redirect(url_for('profile_info', username=username))
        else:
            return jsonify({"status": 401, "result": "Incorrect Username or Password"})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})

@APP.route('/profile_info', methods=['POST','GET'])
def profile_info():
    try:
        if session and session["logged"]:
            username = request.args['username'].upper()
            user = USERDETAIL.query.filter_by(name=username).first()
            user_detail = {
                    "name": user.name,
                    "email": user.email,
                    "phone": user.phone
                    }
            return jsonify({"status": 200, "result":user_detail})
        else:
            return jsonify({"status":200, "result":"Session Expired. Please Login...."})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})
    
@APP.route('/signup', methods=['POST'])
@expects_json(SIGNUP_SCHEMA)
def signup():
    try:
        data = request.get_json()
        if data:
            if data['email'].endswith('@fleetstudio.com'):
                user_exists = USERDETAIL.query.filter_by(email=data['email'].lower()).first()
                print(user_exists)
                if not user_exists:
                    new_user = USERDETAIL(name=data['username'].upper(), passwd=data['password'], \
                                        email=data['email'].lower(), phone=data['phone'])
                    DB.session.add(new_user)
                    DB.session.commit()
                    return jsonify({"status":201, "result": f"User {new_user.name} has been created successfully."})
                else:
                    return jsonify({"status":200, "result": f"User {user_exists.name} Already Exists. Please Login...."})
            else:
                return jsonify({"status":200, "result": "Enter a Valid Email-ID"})
        else:
            return jsonify({"status":400, "result": "Error in JSON format"})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})

@APP.route("/logout")
def logout():
    try:
        if session and session["logged"]:
            #session.pop('logged', None)
            session["logged"] = False
            return jsonify({"status":200, "result":"User Logged Out Successfully"})
        else:
            return jsonify({"status":200, "result":"Session Expired. Please Login...."})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})

if __name__ == '__main__':
    APP.secret_key = os.urandom(12)
    APP.run()
