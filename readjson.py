# readjson.py

import json

def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(data)
	return data

def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)

data = {'123456':['Banana',100,5],
		'123789':['Durian',50,99],
		'136541':['แก้วมังกร',42,20]}

writejson(data)