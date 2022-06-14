from django.shortcuts import render

# Create your views here.
def django (request):
	return render(request, 'ex01/django.html', {'title': 'Django'})

def display (request):
	return render(request, 'ex01/display.html', {'title': 'Display'})

def templates (request):
	return render(request, 'ex01/templates.html', {'title': 'Templates'})