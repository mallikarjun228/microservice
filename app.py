from flask import Flask
from flask import jsonify
app=Flask(__name__)
@app.route('/')
def indecx():
	response_data={}
	response_data['massege']='welcome'
	response_data['status']='success'
	response=jsonify(response_data)
	return response
