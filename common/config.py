#!/usr/bin/python3


import os

DB_TYPE = os.environ.get("DB_TYPE","")
DB_USER = os.environ.get("DB_USER","")
DB_PASSWORD = os.environ.get("DB_PASSWORD","")
INITIALIZE = os.environ.get("INITIALIZE","")
LISTEN = os.environ.get("LISTEN","")
