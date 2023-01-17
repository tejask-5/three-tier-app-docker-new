from flask import Flask, request, jsonify,render_template,redirect, url_for
import requests
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='172.19.8.150'
app.config['MYSQL_USER']='cbc'
app.config["MYSQL_PASSWORD"]='fortinet'
app.config["MYSQL_DB"]='flaskapp'

mysql=MySQL(app)
CORS(app)

@app.route("/registration",methods=['GET','POST'])
def registration():
	cur=mysql.connection.cursor()
	data=request.get_json()
	print("JSON:")
	print(data)
	firstname = data['firstname']
	lastname = data['lastname']
	email = data['email']
	username = data['username']
	password = data['password']
	print(firstname,lastname,email,username,password)
	query="INSERT INTO users VALUES('{}','{}','{}','{}','{}')".format(firstname,lastname,email,username,password)
	print(query)
	cur.execute(query)
	cur.execute("SELECT * FROM users")
	fetchdata=cur.fetchall()
	print(fetchdata)
	mysql.connection.commit()
	cur.close()
	return data

@app.route("/login",methods=['GET','POST'])
def login():
	cur=mysql.connection.cursor()
	data=request.get_json()
	username = data['username']
	password = data['password']
	query="select username from users where username = '" + username + "' and password = '" + password + "';"
	cur.execute(query)
	row = cur.fetchone()
	mysql.connection.commit()
	cur.close()
	if row is not None:
		return jsonify(result="true")
	else:
		return jsonify(result="false")

if __name__ == "__main__":
    app.run(debug= True,port=5000,host='0.0.0.0',ssl_context=('cert.pem', 'key.pem'))
