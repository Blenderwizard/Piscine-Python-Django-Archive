from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def populate(request):
	inputs = [
		("The Phantom Menace", 1, "George Lucas", "Rick McCallum", '1999-05-19'),
		("Attack of the Clones", 2, "George Lucas", "Rick McCallum", '2002-05-16'),
		("Revenge of the Sith", 3, "George Lucas", "Rick McCallum", '2005-05-19'),
		("A New Hope", 4, "George Lucas", "Gary Kurtz, Rick McCallum", '1977-05-25'),
		("The Empire Strikes Back", 5, "Irvin Kershner", "Gary Kurtz, Rick McCallum", '1980-05-17'),
		("Return of the Jedi", 6, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", '1983-05-25'),
		("The Force Awakens", 7, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", '2015-12-11')
	]
	response = []
	for ins in inputs:
		try:
			a,b,d,e,f = ins
			m = Movies(title = a, episode_nb = b, director = d, producer = e, release_date = f)
			m.save()
			response.append("OK")
		except Exception as e:
			response.append(str(e))
	
	return HttpResponse("1: {}<br />2: {}<br />3: {}<br />4: {}<br />5: {}<br />6: {}<br />7: {}<br />".format(
		response[0],
		response[1],
		response[2],
		response[3],
		response[4],
		response[5],
		response[6]
	))

def display(request):
	try:
		data = Movies.objects.all()
	except Exception as e:
		return HttpResponse("No data available")

	if len(data) == 0:
		return HttpResponse("No data available")

	return render(request, 'ex03/view.html', {
		"data": data
	})