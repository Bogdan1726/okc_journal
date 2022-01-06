# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('', index, name='home')
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('queryset/', return_queryset, name='return_queryset'),
    path('city/', render_of_city, name='return_of_city'),
    path('queryset_city', queryset_city, name='return_queryset_city'),
]
