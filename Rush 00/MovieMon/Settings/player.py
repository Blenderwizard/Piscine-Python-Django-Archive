class Player:
	def __init__(self, confinfo: dict) -> None:
		try:
			if (confinfo['gridSizeX'] < 10):
				self.boardxmax = 10
			else:
				self.boardxmax = confinfo['gridSizeX']
		except:
			self.boardxmax = 10
		try:
			if (confinfo['gridSizeY'] < 10):
				self.boardymax = 10
			else:
				self.boardymax = confinfo['gridSizeY']
		except:
			self.boardymax = 10
		try:
			if (confinfo['playerPosStartX'] > self.boardxmax):
				self.x = 0
			else:
				self.x = confinfo['playerPosStartX']
		except:
			self.x = 0
		try:
			if (confinfo['playerPosStartY'] > self.boardymax):
				self.y = 0
			else:
				self.y = confinfo['playerPosStartY']
		except:
			self.y = 0

		self.movieball = 0
		self.caught_movies = []

	def move_up(self) -> bool:
		if self.y  != 0:
			self.y -= 1
			return True
		return False

	def move_down(self) -> bool:
		if self.y  != self.boardymax - 1:
			self.y += 1
			return True
		return False

	def move_left(self) -> bool:
		if self.x  != 0:
			self.x -= 1
			return True
		return False

	def move_right(self) -> bool:
		if self.x  != self.boardxmax - 1:
			self.x += 1
			return True
		return False
	
	def grab_ball(self) -> None:
		self.movieball += 1

	def throw_ball(self) -> None:
		if self.movieball != 0:
			self.movieball -= 1