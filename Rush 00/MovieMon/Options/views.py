from nis import cat
from django.shortcuts import render, redirect
from Settings.config import Cartridge
import os
import pickle

# Create your views here.

slots = ['slota.bin', 'slotb.bin', 'slotc.bin']

def options(request):
	global Cartridge
	if request.method == 'POST':
		if 'A' in request.POST:
			return redirect("/options/save_game")
		if 'B' in request.POST:
			return redirect("/")
		if 'Start' in request.POST:
			return redirect("/worldmap")
	return render(request, 'options/options.html', {
		'title' : 'Load Game',
		'a_enabled': True,
		'b_enabled': True,
		'up_enabled': False,
		'down_enabled': False,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': True,
		'select_enabled': False,
	})

def save(request):
	global Cartridge
	if Cartridge.slotPos < 0 or Cartridge.slotPos >= 3:
		Cartridge.slotPos = 0
	if request.method == 'POST':
		if 'formId' in request.POST:
			if Cartridge.lastformid != int(request.POST['formId']):
				print('no')
			elif 'A' in request.POST:
				Cartridge.dump(slots[Cartridge.slotPos])
			elif 'B' in request.POST:
				return redirect("/options")
			elif 'Up' in request.POST:
				Cartridge.slotPos -= 1
				if Cartridge.slotPos < 0:
					Cartridge.slotPos = 0
			elif 'Down' in request.POST:
				Cartridge.slotPos += 1
				if Cartridge.slotPos >= 3:
					Cartridge.slotPos = 2
	Cartridge.lastformid = Cartridge.current_milli_time()
	data = []
	names = ['A', 'B', 'C']
	for i in slots:
		if os.path.exists(i) and os.stat(i).st_size != 0:
			f = open(i, 'rb')
			d = pickle.load(f)
			e = len(d['player'].caught_movies)
			g = len(d['moviemons'])
			data.append((names[slots.index(i)], e, g))
			f.close()
		else:
			data.append((names[slots.index(i)], 0, 0))
	return render(request, 'options/save.html', {
		'title' : 'Load Game',
		'a_enabled': True,
		'b_enabled': True,
		'up_enabled': True,
		'down_enabled': True,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': False,
		'select_enabled': False,
		'slotpos': Cartridge.slotPos,
		'formid': Cartridge.lastformid,
		'slots': data
	})

def load(request):
	global Cartridge
	if Cartridge.slotPos < 0 or Cartridge.slotPos >= 3:
		Cartridge.slotPos = 0;
	if request.method == 'POST':
		if 'formId' in request.POST:
			if Cartridge.lastformid != int(request.POST['formId']):
				print('no')
			elif 'A' in request.POST:
				if Cartridge.loaded_slot == Cartridge.slotPos:
					Cartridge.loaded_slot = -1
					return redirect("/worldmap")
				else:
					Cartridge.load(slots[Cartridge.slotPos])
					Cartridge.loaded_slot = Cartridge.slotPos
			elif 'B' in request.POST:
				return redirect("/")
			elif 'Up' in request.POST:
				Cartridge.slotPos -= 1
				if Cartridge.slotPos < 0:
					Cartridge.slotPos = 0
			elif 'Down' in request.POST:
				Cartridge.slotPos += 1
				if Cartridge.slotPos >= 3:
					Cartridge.slotPos = 2
	Cartridge.lastformid = Cartridge.current_milli_time()
	data = []
	names = ['A', 'B', 'C']
	for i in slots:
		if os.path.exists(i) and os.stat(i).st_size != 0:
			f = open(i, 'rb')
			d = pickle.load(f)
			e = len(d['player'].caught_movies)
			g = len(d['moviemons'])
			data.append((names[slots.index(i)], e, g))
			f.close()
		else:
			data.append((names[slots.index(i)], 0, 0))
	return render(request, 'options/load.html', {
		'title' : 'Load Game',
		'a_enabled': os.path.exists(slots[Cartridge.slotPos]) and os.stat(slots[Cartridge.slotPos]).st_size != 0,
		'b_enabled': True,
		'up_enabled': True,
		'down_enabled': True,
		'left_enabled': False,
		'right_enabled': False,
		'start_enabled': False,
		'select_enabled': False,
		'slotpos': Cartridge.slotPos,
		'formid': Cartridge.lastformid,
		'slots': data,
		'loaded_slot': Cartridge.loaded_slot
	})