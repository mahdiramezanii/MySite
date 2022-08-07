from django.urls import path
from . import views

app_name="Blog"
urlpatterns=[
    path("",views.Blog_app,name="blog"),
    path("detail/<slug:slug>",views.blog_detail,name="detail"),
    path("search",views.search,name="serach"),
]