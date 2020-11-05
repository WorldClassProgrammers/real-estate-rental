from django.urls import path

from . import views

app_name = 'estate'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('condo/<int:condo_id>/', views.condo, name='condo'),
    path('room/<int:room_id>/', views.room, name='room'),
    path('search', views.search, name='search_results'),
]
