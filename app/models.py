from django.db import models

# Create your models here.


class Userinfo(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    datatime = models.DateTimeField(auto_now=True)


class goods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    goods_id = models.CharField(max_length=100)
    comment_num = models.CharField(max_length=100)


class pad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    goods_id = models.CharField(max_length=100)
    comment_num = models.CharField(max_length=100)


class netbook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    goods_id = models.CharField(max_length=100)
    comment_num = models.CharField(max_length=100)