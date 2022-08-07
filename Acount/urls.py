from django.urls import path
from . import views
app_name="acount"
urlpatterns=[
    path("login",views.login_user,name="login"),
    path("logout",views.logout,name="logout"),
    path("register",views.register_user,name="register")

]