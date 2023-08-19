from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("search",views.search,name="search"),
    path('show_data/<str:pk>/',views.show_data,name='show_data')
]