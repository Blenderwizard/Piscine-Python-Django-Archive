from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('django', views.django, name='django'),
    path('display', views.display, name='display'),
    path('templates', views.templates, name='templates'),
    path('django/', views.django, name='django'),
    path('display/', views.display, name='display'),
    path('templates/', views.templates, name='templates'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)