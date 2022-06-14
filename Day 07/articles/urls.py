from django.urls import path

from . import views

urlpatterns = [
	path('articles', views.articles.as_view(), name='articles'),
	path('publications', views.Publications.as_view(), name='publications'),
	path('publish', views.Publish.as_view(), name='publish'),
	path('favourites', views.Favourites.as_view(), name='favourite'),
	path('articles/<int:pk>', views.Detail.as_view(), name='detail'),
    path('', views.home.as_view(url='/articles'), name='redirect'),
	path('login', views.loginView.as_view(), name='login'),
	path('logout', views.logoutView.as_view(), name='articles'),
	path('register', views.RegisterView.as_view(), name='register'),
]