from django.db import models
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length= 30)
    comment = models.TextField()
    time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="user-photo/",  default="user-photo/karem_photo.jpg")
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Report(models.Model):
    report = models.TextField(max_length=500, default="User-Report-Error")
    def __str__(self):
        return self.report

class Admin(models.Model):
    name_admin = models.CharField(max_length= 30, default="admin-photo")
    image = models.ImageField(upload_to="photoss/%y/%m/%d",default='photo/5.5.jpg')
    activate = models.BooleanField(default=False)

    def __str__(self):
        return self.name_admin


class Edit(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username