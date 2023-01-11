from django.urls import path
from authors import views


urlpatterns = [
    path('create-new-account', views.singUp, name="register"),
    path('login', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout"),

]
