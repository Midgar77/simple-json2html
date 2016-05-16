'''
 * Author: Midgar77
 * JSON to HTML converter
 * 2015
'''

import json
import string

class JSON2HTML:

	#html is a string variable that contains all of the HTML code to create the resulting HTML table
	#data is added to html throughout the convert process
	global html
	html = "<!DOCTYPE><html>"

	#converts input jsonData to HTML table
	def convertToHTML(self, jsonData):
		global html
		#Uses Python's json library to convert json info to python data structures
		pythonData = json.loads(self.fileGetContents(jsonData))
		#Passes the pythonData to the build function to convert JSON info to HTML
		html += self.build(pythonData)
		html += "</html>"
		return html
		

	#Utility function to get contents of a file (used to grab JSON info from a file)
	def fileGetContents(self, filename):
    		with open(filename) as f:
        		return f.read()


	#Recursive method that builds the html table based on the input param pythonData (which must be a python object like a dict, list, str, etc...)
	#Param pythonData should NOT be json format, it should be converted to python data structures before calling this method
	def build(self, pythonData):
		currentHTML = ""
		if type(pythonData) is dict:
			currentHTML += "<table border=\"1\">"
			for key in pythonData:
				currentHTML += "<tr><th>"+str(key)+"</th><td>"+str(self.build(pythonData[key]))+"</td></tr>"
			currentHTML += "</table>"
			return currentHTML
		elif type(pythonData) is list:
			currentHTML += "<table border=\"1\"><tr><td><ul>"
			for i in range(len(pythonData)):
				currentHTML += "<li>"+str(self.build(pythonData[i]))+"</li>"
			currentHTML += "</ul></td></tr></table>"
			return currentHTML
		#base case, when given a python variable like a number or string, just return that value
		else:
			return str(pythonData)


json2html = JSON2HTML()
