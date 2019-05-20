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
	text = request.data.decode('utf-8')
	regex = re.compile('(\W+)')
	freqs = trieProcess(text, regex)

	splitText = regex.split(text)
	return json.dumps(
		list(
			map(lambda string: [string, freqs[string.lower()]], splitText)
			)
		)



if __name__ == "__main__":
	app.run()
