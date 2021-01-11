# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:35:38 2021

@author: Mandar Sudhakar Ghadi
"""

import requests
import json

##################################
#login test cases
def test_login_pass():
    req_data = {'username':'msghadi','password':'1sigm#'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/login', data=json.dumps(req_data),headers=headers)
    print(result.text)
    result = json.loads(result.text)
    assert 'data' in result.keys()

def test_login_fail():
    req_data = {}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/login', data=json.dumps(req_data),headers=headers)
    result = json.loads(result.text)
    assert result['result'] in ['Error in JSON format', 'Incorrect Username or Password']

def test_login_fail2():
    req_data = {'username':'msghadi'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/login', data=json.dumps(req_data),headers=headers)
    result = json.loads(result.text)
    assert result['result'] in ['Error in JSON format', 'Incorrect Username or Password']

def test_login_fail3():
    req_data = {'password':'1sigm#'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/login', data=json.dumps(req_data),headers=headers)
    result = json.loads(result.text)
    assert result['result'] in ['Error in JSON format', 'Incorrect Username or Password']
  

##################################
#singup test cases
def test_signup_pass():
    req_data = {'username':'msghadi','password':'1sigm#', 'email':'mandar.ghadi@fleetstudio.com','phone':'9594203334'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/signup', data=json.dumps(req_data),headers=headers)
    result = json.loads(result.text)
    assert result['result'] not in ['Error in JSON format', 'Enter a Valid Email-ID']

def test_signup_fail():
    req_data = {'username':'msghadi', 'password':'1sigm#'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    session = requests.Session()
    result = session.post('http://localhost:5000/signup', data=json.dumps(req_data),headers=headers)
    print('result', result.text)
    result = json.loads(result.text)
    assert result['result'] in ['Error in JSON format', 'Enter a Valid Email-ID']


##################################
##profile_info test cases.
def test_profileinfo_pass():#Passed. Need to give ID which is in annotation_config table.
    req_data = {'username':'msghadi'} 
    session = requests.Session()
    result = session.get('http://localhost:5000/profile_info', params=req_data)
    print(result.text)
    result = json.loads(result.text)
    assert 'data' in result.keys() or result['result'] in ['Session Expired. Please Login....']

def test_profileinfo_fail():
    req_data = {}
    session = requests.Session()
    result = session.get('http://localhost:5000/profile_info', params=req_data)
    result = json.loads(result.text)
    assert result['result'] in ['Username not passed', 'Session Expired. Please Login....']


