from  django.urls import path
from . import views
urlpatterns=[
    
    path('add/', views.add, name='add'),
    path('department/', views.department, name='department'),
    path('edit/', views.edit, name='edit'),
    path('home/', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('search/', views.search, name='search'),
    path('search/search_ajax/', views.search_ajax, name='search_ajax'),

    path('view/', views.view, name='view'),


]