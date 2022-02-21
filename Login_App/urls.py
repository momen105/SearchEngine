from django.urls import path
from Login_App import views

app_name = "Login_App"

urlpatterns = [

    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]
