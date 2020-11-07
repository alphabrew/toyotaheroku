from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('get_url/', views.get_url,),
    path('get_url/get_prices', views.get_prices,),
    
]
