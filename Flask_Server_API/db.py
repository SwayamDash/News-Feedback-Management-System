from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://swayam:swayam123@cluster0.wiqoj.mongodb.net/newsfeedbacksystem?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('newsfeedbacksystem')
store = pymongo.collection.Collection(db, 'store')