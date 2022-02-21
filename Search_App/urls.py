from django.urls import path
from Search_App import views

app_name = "Search_App"

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('search/', views.search, name='search'),
    path('filter_search/', views.filter, name='filter'),

]
