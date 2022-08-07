from django.db import models


class resume(models.Model):
    titel=models.CharField(max_length=50)
    data=models.CharField(max_length=100)
    text=models.TextField()


    def __str__(self):

        return self.titel

class eduction(models.Model):
    titel=models.CharField(max_length=50)
    data=models.CharField(max_length=100)
    text=models.TextField()


    def __str__(self):

        return self.titel


class maharat(models.Model):

    langoag=models.CharField(max_length=50)
    count_langoag=models.CharField(max_length=50)


