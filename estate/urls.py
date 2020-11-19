from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


app_name = 'estate'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('condo/<int:condo_id>/', views.condo, name='condo'),
    path('unit/<int:unit_id>/', views.unit, name='unit'),
    path('search/', views.search, name='search_results'),

    path('upload/', views.upload_index, name='upload_index'),
    path('upload/condo/', views.upload_condo, name='upload_condo'),
    path('upload/unit/', views.upload_unit, name='upload_unit'),
    path('upload/owner/', views.upload_owner, name='upload_owner')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
