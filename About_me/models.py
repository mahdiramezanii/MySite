from django.db import models

class About(models.Model):

        name=models.CharField(max_length=50)
        image=models.ImageField(upload_to="About_me/image",null=True)
        city=models.CharField(max_length=50)
        text=models.TextField()
        tajrobeh=models.CharField(max_length=20)
        count_project=models.CharField(max_length=20)




