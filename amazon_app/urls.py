from django.urls import path
from . import views

urlpatterns = [
    path('amazon_search', views.amazon_search, name='amazon_search'),
    path('', views.home, name='home'),
]