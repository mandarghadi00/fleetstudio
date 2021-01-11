# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

import os
from datetime import timedelta
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_expects_json import expects_json
from config import SIGNUP_SCHEMA, LOGIN_LST, SIGNUP_LST
from models import UserDetail
from base import Session

APP = Flask('FleetStudio')

APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@APP.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if all(keys in data for keys in LOGIN_LST):
            username = data['username'].upper()
            password = data['password']
            sess = Session()
            user = sess.query(UserDetail).filter_by(name=username, passwd=password).first()
            sess.close()
            if user:
                session["logged"] = True
                session.permanent = True
                APP.permanent_session_lifetime = timedelta(minutes=5)
                return redirect(url_for('profile_info', username=username))
            else:
                return jsonify({"status": 401, "result": "Incorrect Username or Password"})
        else:
            return jsonify({"status":400, "result": "Error in JSON format"})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})

@APP.route('/profile_info', methods=['POST','GET'])
def profile_info():
    try:
        if session and session["logged"]:
            if request.args:
                username = request.args['username'].upper()
                sess = Session()
                user = sess.query(UserDetail).filter_by(name=username).first()
                sess.close()
                user_detail = {
                        "name": user.name,
                        "email": user.email,
                        "phone": user.phone
                        }
                return jsonify({"status": 200, "data":user_detail})
            else:
                return jsonify({"status": 400, "result":"Username not passed"})
        else:
            return jsonify({"status":200, "result":"Session Expired. Please Login...."})
    except Exception as exception:
        return jsonify({"status": 500, "result": exception})
    
@APP.route('/signup', methods=['POST'])
@expects_json(SIGNUP_SCHEMA)
def signup():
    try:
        data = request.get_json()
        if all(keys in data for keys in SIGNUP_LST):
            if data['email'].endswith('@fleetstudio.com'):
                sess = Session()
                user_exists = sess.query(UserDetail).filter_by(email=data['email'].lower()).first()
                if not user_exists:
                    sess = Session()
                    new_user = UserDetail(name=data['username'].upper(), passwd=data['password'], \
                                        email=data['email'].lower(), phone=data['phone'])
                    sess.add(new_user)
                    sess.commit()
                    user_name = new_user.name
                    sess.close()
                    return jsonify({"status":201, "result": f"User {user_name} has been created successfully."})
                else:
                    sess.close()
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
    APP.run(host = '0.0.0.0', port = 5000, debug = True)
