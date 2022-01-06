from django.urls import path
from .views import *

urlpatterns = [
    #path('', stat.index, name='statistic'),
    path('', StatisticCalls.as_view(), name='statistic'),
    #path('add/', stat.statistic_add, name='add_statistic'),
    path('add/', statistic_add, name='add_statistic')

]
