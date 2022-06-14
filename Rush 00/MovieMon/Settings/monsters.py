import requests
import json

class Monster:
	def __init__(self, name: str) -> None:
		url = 'http://www.omdbapi.com/?i=tt3896198&apikey=51bf8868'
		parameter = {
			't' : name,
			'type': 'movie'
		}
		r = requests.get(url, parameter)
		self.data = json.loads(r.text)
		self.name = self.data['Title']
		self.id = self.data['imdbID']
		self.poster = self.data['Poster']
		self.director = self.data['Director']
		self.year = self.data['Year']
		self.rating = self.data['Rated']
		self.synopsis = self.data['Plot']
		self.strength = self.data['imdbRating']
		self.actors = self.data['Actors']

	def get_strength(self) -> float:
		return float(self.strength)

	def __str__(self) -> str:
		return str(self.data)
