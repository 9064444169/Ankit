from tkinter import CASCADE

from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)
class Malware_Recogition_Model(models.Model):
    usid=models.ForeignKey(RegisterModel)
    links=models.CharField(max_length=500)
    result=models.CharField(max_length=500)
class FeedbackModel(models.Model):
    uid=models.ForeignKey(RegisterModel)
    feedback=models.CharField(max_length=100)