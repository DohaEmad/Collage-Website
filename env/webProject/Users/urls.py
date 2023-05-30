from re import template
from django.urls import path
from django.contrib.auth import views as loginn
from . import views
urlpatterns=[
   # path('login/', loginn.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('login/',views.login,name='login')

]
