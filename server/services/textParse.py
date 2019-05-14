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
		-> 1 is the count of instances that this node has been visited over all insert processes
'''
TRIE = [{}]

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
			node[0][charCode] = [{}, 0]

		node = node[0][charCode]
		# increment the amount of visits to this node
		node[1] += 1
			
	return node[1]

'''
	traverse through the trie.
	if
		-> the string has NOT been inserted before
			-> return true
		-> the string has been inserted before
			-> return false
'''
def _has(string):
	node = TRIE[ord(string[0])]

	for c in range(1, len(string)):
		charCode = ord(string[c])

		if not node[charCode] in globals():
			return False

		node = node[charCode][0]

	return True

def trieProcess(stringArray = [], regex = DEFAULT_REGEX):
	stringSet = {}
	for s in stringArray:
		stringSet[s] = _insert(s)
	
	TRIE[0].clear()
	return stringSet
