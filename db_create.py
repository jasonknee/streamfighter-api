#!flask/bin/python
from streamfighter import db
from streamfighter.models import *

db.create_all()

# print("DB created.")
