# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:09:10 2021

@author: Mandar Sudhakar Ghadi
"""

POSTGRES_URI = "postgresql://postgres:postgres@localhost:5432/fleetstudio"

SIGNUP_SCHEMA = {
        'type': 'object',
        'properties': {
            'username': {'type': 'string',
                         "maxLength": 8},
            'email': {'type': 'string'},
            'password': {'type': 'string',
                         "pattern": "^(?=.{6,})(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[#_-]).*$",
                         "maxLength": 6},
            'phone': {'type': 'string',
                      "minLength": 10,
                      "maxLength": 10}
        },
        'required': ['username', 'password']
        }

LOGIN_LST = ("username", "password")
SIGNUP_LST = ("username", "password", "email", "phone")