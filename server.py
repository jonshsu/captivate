import flask
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku
app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

class SpreadsheetData(db.Model):
    __tablename__ = "spreadsheetdata"
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

    def __init__ (self, mydata):
        self.mydata = mydata

@app.route("/")
def index():
	rows = [str(i+1) for i in range(10)]
	columns = [chr(i+ord('A')) for i in range(10)]
	return flask.render_template('index.html', rows=rows, columns=columns)

@app.route("/exceldata", methods=['POST', 'GET'])
def exceldata():
	if request.method == 'POST':
		# indata = SpreadsheetData(request.get_json())
		try:
			sheet = SpreadsheetData.query.filter_by(id='1').first()
			sheet.mydata = request.get_json()
			# db.session.add(indata)
			db.session.commit()
		except Exception as e:
			print(e)
			sys.stdout.flush()
		# return 'Success'
		return e

	elif request.method == 'GET':
		try:
			outdata = SpreadsheetData.query.filter_by(id='1').first()
			return json.jsonify(outdata)
		except Exception as e:
			# print(e)
			# sys.stdout.flush()
			# return 'Failure'
			return e

if __name__ == ' __main__':
	#app.debug = True
	app.run()