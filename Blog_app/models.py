from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class article(models.Manager):

    def published(self):


        return self.filter(status=True)


class Blog(models.Model):

    wrter=models.CharField(max_length=50)
    titel=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    text=models.TextField()
    image=models.ImageField(upload_to="blog/image")
    slug=models.SlugField(unique=True,blank=True,null=True,allow_unicode=True)
    status=models.BooleanField(default=True)
    objects=article()
    category=models.ManyToManyField(Category,related_name="Blog")

    def get_absolut_url(self):


        return reverse("Blog:detail",kwargs={"slug":self.slug})

    def save(self,*args,**kwargs):
       self.slug=slugify(self.titel)

       super(Blog, self).save(*args,**kwargs)



    def show_text(self):


        return self.text[:200]

    def __str__(self):

        return self.titel



class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_comment")
    article=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comment")
    created=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replay")


    def __str__(self):

        return self.body[0:10]



