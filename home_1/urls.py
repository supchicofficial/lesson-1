from django.urls import path
from .views import *

urlpatterns = [
    path('get_name/<str:name>/', get_name),
    path('get_sername/<str:sername>/', get_sername),
    path('get_age/<str:age>/', get_age),
    path('get_birthday/<str:birthday>/', get_birthday),
    path('get_long/<str:long>/', get_long),
]