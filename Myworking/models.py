from django.db import models

class Working(models.Model):
    name=models.CharField(max_length=50)
    titel=models.CharField(max_length=50)
    image=models.ImageField(upload_to="Myworking/img")


    def __str__(self):

        return self.titel


