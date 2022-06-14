from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.dex, name="Moviedex"),
	path('/', views.dex, name="Moviedex"),
	path('/<str:id>', views.info, name="Moviemon Info"),
	path('/<str:id>/', views.info, name="Moviemon Info"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)