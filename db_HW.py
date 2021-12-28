import mongoengine.fields
import pymongo
from mongoengine import *

connect('pupils')

class User(Document):
    enter_date = mongoengine.fields.DateField()
    School_N = StringField
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    average_mark = StringField(max_length=20, required=True)

#
ross = User(email='invanov.vas@google.com', first_name='Ivanovich', last_name='Vasil').save()