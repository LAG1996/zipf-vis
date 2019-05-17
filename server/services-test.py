import json
import re
import sys

from services.textParse import trieProcess

def textParse():
	testString = 'This this this this is a test striiiiing!!!! 0000 00 0 2 22 22 2'
	return (
		json.dumps(
			trieProcess(
				testString,
				re.compile('(\W|\s)')
			)
		)
	)

options = {
	'textParse': textParse
}

if sys.argv[1] in options:
	result = options[sys.argv[1]]()
	print(str(result))
else:
	print('I do not recognize that service.')