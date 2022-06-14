from .player import Player
from .monsters import Monster

import time
import random
import pickle
import copy

confinfo = {
	"gridSizeX" : 10,
	"gridSizeY" : 10,
	"playerPosStartX" : 5,
	"playerPosStartY" : 5,
	"imdName" : [
		"Sharknado",
		"Sharknado 2: The Second One",
		"Sharknado 3: Oh Hell No!",
		"Sharknado 4: The 4th Awakens",
		"Sharknado 5: Global Swarming",
		"The Last Sharknado: It's About Time",
		"Interstellar",
		"Inception",
		"Avengers: Endgame",
		"Halloween H20: 20 Years Later",
		"The Lord of the Rings: The Fellowship of the Ring",
		"Dragonball Evolution",
		"The Grinch",
		"Super Mario Bros.",
		"The Fast and the Furious: Tokyo Drift"
	]
}

class GameCartridge():
	def __init__(self):
		self.slotPos = 0
		self.player = Player(confinfo)
		self.moviemons = {}
		self.lastformid = 0
		self.dexPos = 0
		self.loaded_slot = -1

	def load(self, slot: str):
		f = open(slot, 'rb')
		data = pickle.load(f)
		f.close()
		self.__dict__.clear()
		self.__dict__.update(data)

	def dump(self, slot: str):
		f = open(slot, 'wb')
		data = copy.deepcopy(self.__dict__)
		pickle.dump(data,f)
		f.close()
	
	def get_random_movie(self):
		temp = self.moviemons.copy()
		for i in self.player.caught_movies:
			del temp[i.id]
		return random.choice(list(temp.values()))

	def load_default_settings(self, confinfo: dict):
		self.player = Player(confinfo)
		self.lastformid = 0
		self.moviemons = {}
		self.dexPos = 0
		self.slotPos = 0
		for i in confinfo['imdName']:
			monster = Monster(i)
			self.moviemons[monster.id] = monster
	
	def get_strength(self) -> int:
		return len(self.player.caught_movies)

	def get_movie_from_key(self, key: str):
		for k, value in self.moviemons.items():
			if key == k:
				return value

	def get_movie(self, name: str):
		for key, value in self.moviemons.items():
			if name == value.name:
				return value

	def get_difficulty_score(self, id: str) -> int:
		if id in self.moviemons:
			score = 50 - (self.moviemons[id].get_strength() * 10) + (self.get_strength() * 5)
			if score < 1:
				score = 1
			if score > 90:
				score = 90
			return score

	@staticmethod
	def current_milli_time():
		return round(time.time() * 1000)

Cartridge = GameCartridge()
