from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests



app = Flask(__name__, static_folder="static")

@app.route('/api/v1/album', methods=['GET'])
def album_json():
	album_info = os.path.join(app.static_folder, 'data','album.json')
	with open(album_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/api/v1/movies', methods=['GET'])
def movies_json():
	movies_info = os.path.join(app.static_folder, 'data','movies.json')
	with open(movies_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/api/v1/organizedmovies', methods=['GET'])
def organizedmovies_json():
	json_info =''
	organizedmovies_info = os.path.join(app.static_folder, 'data','movies.json')
	with open(organizedmovies_info, 'r') as json_data:
		json_info = json.load(json_data) 
	results=[]

	if 'title' in request.args:
		title = request.args['title']

		for movie in json_info:
			results.append(movie)
	return render_template('movies.html', results=results)	


@app.route('/')
def index():
	name = 'Kathrin'
	friends = ['Marie', 'Annika', 'Isabela']
	countries = ['Turkey', 'Argentina', 'Japan']
	return render_template('index.html', greeting=name, friends=friends, countries=countries)


@app.route('/about')
def about():
	return '<h1>About</h1><p>learning about me</p>'


@app.route('/Nasa')
def show_nasa_pic():
	today = str(date.today())
	response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
	data = response.json()
	return render_template('nasa.html', data=data)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')