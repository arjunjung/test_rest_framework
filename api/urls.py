from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('toys/',views.toy_list,name='toy_list'),
    path('toys/<int:pk>',views.toy_funs,name='toy_funs'),
]
