from flask import Flask, request, jsonify,render_template,redirect, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)
here=""
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route("/addrec", methods=['GET','POST'])
def addrec():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		username = request.form['username']
		password = request.form['password']
		here=request.form
		requests.post('http://ad4ce629c560e414a9d0a78340317c79-0615611bc2c7597a.elb.ap-southeast-1.amazonaws.com/registration',json=dict(here),verify=False)
	return render_template('thanks.html')

@app.route("/chkrec", methods=['GET','POST'])
def chkrec():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		here=request.form
		response = requests.get('http://ad4ce629c560e414a9d0a78340317c79-0615611bc2c7597a.elb.ap-southeast-1.amazonaws.com/login',json=dict(here),verify=False)
		response_dict = json.loads(response.text)
		result = response_dict["result"]

	if result == "true":
		return render_template('success.html')
	else:
		return render_template('fail.html')

if __name__ == "__main__":
	app.run(debug= True,port=5001,host="0.0.0.0")
