from django.urls import path

from . import views

app_name = 'estate'
urlpatterns = [
    path('', views.index, name='index')
]
