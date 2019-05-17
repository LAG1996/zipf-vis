'''
	@author: Luis Angel Garcia
'''

import json
import re

DEFAULT_REGEX = re.compile('/\w|\d/')

# create the trie
'''
each node is a duple
	where
		-> 0 is a 'branch', or a pointer to another node further down the tree
		-> 1 is the count of full words that end with this node
		-> 2 is the count of all substrings that end with this node
'''
TRIE = [{}, 0, 0]

'''
	@explanation:
		iterate through the string, creating a node
		that represents the end of each substring in that string

	@params
		`string`: the string to be inserted in the trie
'''
def _insert(string):
	node = TRIE

	'''
		iterate through each character in the string
		each character represents a node in the trie
	'''
	for c in range(0, len(string)):
		charCode = ord(string[c])
		# if this node does not exist, we insantatiate it
		if not charCode in node[0]:
			node[0][charCode] = [{}, 0, 0]

		node = node[0][charCode]

		# increment the amount of visits to this node
		node[2] += 1
	
	# increment the amount of stops to at this node
	node[1] += 1
	return node[1]

def trieProcess(string = [], regex = DEFAULT_REGEX):
	stringSet = {}
	stringArray = regex.split(string)
	for s in stringArray:
		if s.isspace() or len(s) == 0:
			continue

		stringSet[s.lower()] = _insert(s.lower())
	
	TRIE[0].clear()
	return stringSet
