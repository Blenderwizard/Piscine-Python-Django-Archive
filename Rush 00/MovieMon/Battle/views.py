from django.shortcuts import render, redirect
from Settings.config import Cartridge

import random

# Create your views here.

def catch_attempt(id: str):
	global Cartridge
	Cartridge.player.throw_ball()
	score = Cartridge.get_difficulty_score(id)
	print(score)
	if score >= random.randint(1, 100):
		Cartridge.player.caught_movies.append(Cartridge.get_movie_from_key(id))


def battle(request, id :str):
	global Cartridge
	if id not in Cartridge.moviemons:
		return redirect('/worldmap')
	if Cartridge.get_movie_from_key(id) in Cartridge.player.caught_movies:
		return redirect('/worldmap')
	if request.method == 'POST':
		if 'B' in request.POST:
			return redirect('/worldmap')
		if 'formId' in request.POST:
			if Cartridge.lastformid != int(request.POST['formId']):
				print("no")
			elif 'A' in request.POST:
				catch_attempt(id)
	Cartridge.lastformid = Cartridge.current_milli_time()
	return render(request, 'battle.html', {
		'title' : 'Battle',
		'path' : '',
		'a_enabled': Cartridge.player.movieball > 0 and Cartridge.get_movie_from_key(id) not in Cartridge.player.caught_movies,
		'b_enabled': True,
		'up_enabled': False,
		'down_enabled': False,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': False,
		'select_enabled': False,
		'formid': Cartridge.lastformid,
		'movieball_count': Cartridge.player.movieball,
		'id': id,
		'caught': Cartridge.get_movie_from_key(id) in Cartridge.player.caught_movies,
		'movieinfo': Cartridge.get_movie_from_key(id)
	})
