from django.http import HttpResponseRedirect
from django.shortcuts import render
import logging

logger = logging.getLogger("formMemory")

from .forms import ex02Form

def index(request):
	if request.method == 'POST':
		form = ex02Form(request.POST)
		if form.is_valid():
			logger.debug(form.cleaned_data['content'])
			form = ex02Form()
	else:
		form = ex02Form()

	return render(request, 'ex02/index.html', {'form': form})