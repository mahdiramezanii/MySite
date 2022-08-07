from django.urls import path
from . import views

app_name="Home"
urlpatterns=[

    path("",views.Home,name="Home")

]