from django.urls import path
from fotografia import views

urlpatterns = [
    path('', views.index, name='home'),
    path('corretores/', views.list_corretores, name='list-corretores')
]