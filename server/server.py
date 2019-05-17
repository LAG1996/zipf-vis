from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import re

from services.textParse import trieProcess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mike sucks'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/word-freq": {"origins":"http://localhost:port"}})

@app.route('/word-freq', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def output():
	return (
		json.dumps(
			trieProcess(
				json.dumps(request.data),
				re.compile('\W+')
			)
		)
	)

if __name__ == "__main__":
	app.run()
