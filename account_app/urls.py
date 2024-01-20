from django.urls import path
from . import views
urlpatterns = [

    path('singin' , views.SingIn),
    path('singup' , views.SingUp),
    path('logout' , views.Logout),
]