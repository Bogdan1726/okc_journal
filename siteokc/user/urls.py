from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', index, name='profile')
]
