from django.shortcuts import render
from About_me.models import About
from My_resume.models import resume,maharat,eduction
from Myworking.models import Working
from Blog_app.models import Blog
from Cuntact_us.models import contact
from contact_by_me.models import contact_by_me
from Blog_app.models import comment
def Home(request):


    about_me=About.objects.last()
    Resume=resume.objects.all()
    Maharat=maharat.objects.all()
    Eduction=eduction.objects.all()
    working=Working.objects.all()
    blog=Blog.objects.all()[0:5]
    contactt=contact_by_me.objects.all().last()
    Comment=comment.objects.all()[:5]

    if request.method=="POST":

        name=request.POST.get("name")
        email=request.POST.get("email")
        text=request.POST.get("text")

        if name and email and text:
            contact.objects.create(name=name,email=email,text=text)



    return render(request,"Home_app/index.html",context={"ABOUT":about_me,"resume":Resume,"maharat":Maharat,"eduction":Eduction,"working":working,"blog":blog,"contact":contactt,"comment":Comment})
