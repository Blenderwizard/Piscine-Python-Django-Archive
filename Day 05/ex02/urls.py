from django.urls import path

from . import views

urlpatterns = [
    path('init', views.index, name='index'),
    path('init/', views.index, name='index'),
    path('populate', views.populate, name='populate'),
    path('populate/', views.populate, name='populate'),
	path('display', views.display, name='display'),
	path('display/', views.display, name='display'),
]