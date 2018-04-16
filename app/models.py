from django.db import models

# Create your models here.


class Userinfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    datatime = models.DateTimeField(auto_now=True)
