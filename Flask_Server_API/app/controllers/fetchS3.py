from app import app
from flask import render_template, request, jsonify
import os
import db
import json
from bson import json_util

@app.route('/')
def main():
	x = list(db.store.find({"story_date":request.args['date']},{"_id":0}))
		
	return jsonify({'data': x})

