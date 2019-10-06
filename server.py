import flask
from flask import Flask, request, json

app = Flask(__name__)

mydict = {
	"A": { 1: "ASDF", 2: "==", 3: "=hi", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"B": { 1: "Jon", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"C": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"D": { 1: "1", 2: "2", 3: "=D1+D2", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"E": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"F": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"G": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"H": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"I": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" },
	"J": { 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "" }
}

@app.route("/")
def index():
	rows = [str(i+1) for i in range(10)]
	columns = [chr(i+ord('A')) for i in range(10)]
	return flask.render_template('index.html', rows=rows, columns=columns)

@app.route("/exceldata", methods=['POST', 'GET'])
def exceldata():
	global mydict
	if request.method == 'POST':
		mydict = request.get_json()
		return ""

	elif request.method == 'GET':
		return json.jsonify(mydict)
