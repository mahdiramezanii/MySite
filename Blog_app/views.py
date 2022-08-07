from django.shortcuts import render
from Blog_app.models import Blog,comment,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def Blog_app(request):
    category=Category.objects.all()
    blog=Blog.objects.all()
    article_list=Paginator(blog,1)
    pagenumber=request.GET.get("page")
    try:
        show_artice=article_list.page(pagenumber)

    except EmptyPage:
        show_artice = article_list.page(1)

    except PageNotAnInteger:
        show_artice = article_list.page(1)


    return render(request,"Blog_app/blog.html",context={"blog":show_artice,"category":category})


def search(request):
    text=request.GET.get("text")

    blog = Blog.objects.filter(text__icontains=text)
    article_list = Paginator(blog, 1)
    pagenumber = request.GET.get("page")
    try:
        show_artice = article_list.page(pagenumber)

    except EmptyPage:
        show_artice = article_list.page(1)

    except PageNotAnInteger:
        show_artice = article_list.page(1)


    return render(request,"Blog_app/blog.html",{"blog":show_artice})


def blog_detail(request,slug):

    b=Blog.objects.get(slug=slug)


    if request.method=="POST":
        bo=request.POST.get("body")
        parent=request.POST.get("parent_id")

        Comment=comment.objects.create(article=b,user=request.user,body=bo,parent_id=parent)



    return render(request,"Blog_app/blog_detail.html",context={"blog":b})