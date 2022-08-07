from django.db import models

class contact_by_me(models.Model):
    instagram=models.CharField(max_length=100,default="https://www.instagram.com/")
    yotube=models.CharField(max_length=100,default="https://www.youtube.com/")
    telegram=models.CharField(max_length=100,default="https://tlgrm.me/")
    whatsapp=models.CharField(max_length=100,default="https://wa/me/")
    phone=models.CharField(max_length=20)
    addres=models.TextField()
    email=models.EmailField()

