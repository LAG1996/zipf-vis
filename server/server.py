from flask import Flask
from flask_cors import CORS, cross_origin
import json
import re

from services.textParse import trieProcess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mike sucks'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/output": {"origins":"http://localhost:port"}})

@app.route('/output', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def output():
	testArr = re.split('\s', 'aaa aaa aaa bbb ccc bbb aaa')
	return json.dumps(trieProcess(testArr))

if __name__ == "__main__":
	app.run()
