from django.shortcuts import render, redirect
from Settings.config import Cartridge, confinfo

import random

def index(request):
	global Cartridge
	if request.method == 'POST':
		if 'A' in request.POST:
			Cartridge.load_default_settings(confinfo)
			return redirect("/worldmap")
		if 'B' in request.POST:
			return redirect("/options/load_game")
	return render(request, 'index.html', {
		'title' : 'Title Screen',
		'a_enabled': True,
		'b_enabled': True,
		'up_enabled': False,
		'down_enabled': False,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': False,
		'select_enabled': False,
	})
	
encounter = 0

def worldmap(request):
	global Cartridge
	global encounter
	if request.method == 'POST':
		if 'Start' in request.POST:
			return redirect("/options")
		if 'Select' in request.POST:
			return redirect("/moviedex")
		if 'formId' in request.POST:
			if Cartridge.lastformid != int(request.POST['formId']):
				print('no')
			elif 'A' in request.POST:
				if encounter == 1:
					Cartridge.player.grab_ball()
					encounter = 0
				elif encounter == 2:
					battle = Cartridge.get_random_movie()
					path = "/battle/" + battle.id
					return redirect(path)
			elif 'Up' in request.POST:
				if Cartridge.player.move_up():
					encounter = random.choice([0, 0, 0, 1, 1, 2])
			elif 'Down' in request.POST:
				if Cartridge.player.move_down():
					encounter = random.choice([0, 0, 0, 1, 1, 2])
			elif 'Left' in request.POST:
				if Cartridge.player.move_left():
					encounter = random.choice([0, 0, 0, 1, 1, 2])
			elif 'Right' in request.POST:
				if Cartridge.player.move_right():
					encounter = random.choice([0, 0, 0, 1, 1, 2])
	else:
		encounter = 0
	if encounter == 2 and len(Cartridge.player.caught_movies) == len(Cartridge.moviemons):
		encounter = 0
	Cartridge.lastformid = Cartridge.current_milli_time()
	return render(request, 'worldmap.html', {
		'title' : 'Worldmap',
		'path' : '',
		'a_enabled': encounter,
		'b_enabled': False,
		'up_enabled': True,
		'down_enabled': True,
		'left_enabled': True,
		'right_enabled': True,
		'start_enabled': True,
		'select_enabled': True,
		'formid': Cartridge.lastformid,
		'movieball_count': Cartridge.player.movieball,
		'rows': range(0,Cartridge.player.boardymax),
		'cols': range(0,Cartridge.player.boardxmax),
		'player': Cartridge.player,
		'encounter_ball': encounter == 1,
		'encounter_moviemon': encounter == 2
	})