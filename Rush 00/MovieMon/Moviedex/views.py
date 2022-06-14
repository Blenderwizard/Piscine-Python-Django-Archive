from django.shortcuts import render, redirect
from Settings.config import Cartridge

def id_to_movie_name(id: int) -> str:
	return "The Martian"

# Create your views here.
def dex(request):
	global Cartridge
	if Cartridge.dexPos > len(Cartridge.player.caught_movies):
		Cartridge.dexPos = len(Cartridge.player.caught_movies)
	if request.method == 'POST':
		if 'Select' in request.POST:
			return redirect("/worldmap")
		if 'formId' in request.POST:
			if Cartridge.lastformid != int(request.POST['formId']):
				print("no")
			elif 'A' in request.POST:
				return redirect("/moviedex/" + Cartridge.player.caught_movies[Cartridge.dexPos].id)
			elif 'Up' in request.POST:
				Cartridge.dexPos -= 5
				if Cartridge.dexPos < 0:
					Cartridge.dexPos = 0
			elif 'Down' in request.POST:
				Cartridge.dexPos += 5
				if Cartridge.dexPos < len(Cartridge.player.caught_movies):
					Cartridge.dexPos = len(Cartridge.player.caught_movies)
			elif 'Left' in request.POST:
				Cartridge.dexPos -= 1
				if Cartridge.dexPos <= 0:
					Cartridge.dexPos = 0
			elif 'Right' in request.POST:
				Cartridge.dexPos += 1
				if Cartridge.dexPos >= len(Cartridge.player.caught_movies):
					Cartridge.dexPos = len(Cartridge.player.caught_movies) - 1
	Cartridge.lastformid = Cartridge.current_milli_time()
	return render(request, 'moviedex/moviedex.html', {
		'title' : 'Moviedex',
		'path' : '',
		'a_enabled': len(Cartridge.player.caught_movies) > 0,
		'b_enabled': False,
		'up_enabled': True,
		'down_enabled': True,
		'left_enabled': True,
		'right_enabled': True,
		'start_enabled': False,
		'select_enabled': True,
		'formid': Cartridge.lastformid,
		'movies': Cartridge.player.caught_movies,
		'caught': len(Cartridge.player.caught_movies),
		'total' : len(Cartridge.moviemons),
		'dexpos' : Cartridge.dexPos

	})

def info(request, id = "0"):
	global Cartridge
	if id not in Cartridge.moviemons:
		return redirect("/moviedex")
	if request.method == 'POST':
		if 'B' in request.POST:
			return redirect("/moviedex")
	return render(request, 'moviedex/info.html', {
		'title' : 'Moviedex',
		'path' : '',
		'a_enabled': False,
		'b_enabled': True,
		'up_enabled': False,
		'down_enabled': False,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': False,
		'select_enabled': False,
		'id': id,
		'movieinfo': Cartridge.get_movie_from_key(id)
	})