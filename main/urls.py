from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flat/', views.flat, name='flat'),
    path('car/', views.car, name='car'),
    path('bike/', views.bike, name='bike'),
    path('laptop/', views.laptop, name='laptop'),
    path('mobile/', views.mobile, name='mobile'),
    path('more/', views.more, name='more'),
]