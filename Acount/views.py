from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.template.context_processors import request
from django.urls import reverse

def login_user(request):
    if request.user.is_authenticated:
        return redirect("Home:Home")

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user is not  None:

            login(request,user)
            return redirect("Home:Home")

        else:
            return redirect("acount:login")



    return render(request,"Acount/login.html")


def logout_user(request):

    logout(request)

    return render(request,"Home_app/index.html")

def register_user(request):

    context={
        "errors":[]
    }

    if request.method=="POST":

        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password2 != password1:
            context["errors"].append("رمز ها شباهت ندارد")
            return render(request,"Acount/register.html",context)

        elif User.objects.filter(username=username).exists():
            context["errors"].append("نام کاربری از قبل وجود دارد")
            return render(request, "Acount/register.html", context)
        elif User.objects.filter(email=email).exists():
            context["errors"].append("ایمیل تکراری است")
            return render(request, "Acount/register.html", context)
        else:
            user=User.objects.create(username=username,email=email,password=password1)

            user.set_password(password1)
            user.save()
            return redirect("Home:Home")





    return render(request,"Acount/register.html")