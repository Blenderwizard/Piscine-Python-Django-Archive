from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('/load_game', views.load, name='load game'),
	path('/save_game', views.save, name='save game'),
	path('/load_game/', views.load, name='load game'),
	path('/save_game/', views.save, name='save game'),
	path('', views.options, name='options'),
	path('/', views.options, name='options')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)