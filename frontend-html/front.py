from flask import Flask, request, jsonify,render_template,redirect, jsonify, Response
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
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/registration')
@app.route('/registration/')
def registration():
    return render_template('registration-on11APR.html')

@app.route("/addrec", methods=['GET','POST'])
@app.route("/addrec/", methods=['GET','POST'])
def addrec():
	if request.method == 'POST':
		here=request.form
		Headers = { 'FSI_APIKEY' : '37JFybUZjpojWEa9GzCM536RGkw56RutMPYu8Vj8' }
		response = requests.post('http://seahk-is-fwb-internal-5cf4808a9027dc93.elb.ap-southeast-1.amazonaws.com/registration',headers = Headers, json=dict(here))

	if response.status_code == 200:
		return render_template('thanks-changedon11APR.html')
	else:
		return Response(response.content, response.status_code)

@app.route("/chkrec", methods=['GET','POST'])
@app.route("/chkrec/", methods=['GET','POST'])
def chkrec():
	if request.method == 'POST':
		here=request.form
		Headers = { 'FSI_APIKEY' : '37JFybUZjpojWEa9GzCM536RGkw56RutMPYu8Vj8' }
		response = requests.post('http://seahk-is-fwb-internal-5cf4808a9027dc93.elb.ap-southeast-1.amazonaws.com/login',headers = Headers, json=dict(here))

	if response.status_code == 200:
		response_dict = json.loads(response.text)
		result = response_dict["result"]
		if result == "true":
			return render_template('success.html')
		else:
			return render_template('fail-on11APR.html')
	else:
		return Response(response.content, response.status_code)

if __name__ == "__main__":
    app.run(debug= True,port=5001,host="0.0.0.0")
