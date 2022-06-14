from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('/<str:id>', views.battle, name="Battle"),
	path('/<str:id>/', views.battle, name="Battle"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)