from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('level/', views.level, name='level_select'),
    path('easyQ/', views.easyQ, name='easy_select'),  
    path('medQ/', views.medQ, name='medium_select'),  
    path('hardQ/', views.hardQ, name='hard_select'),  
]
