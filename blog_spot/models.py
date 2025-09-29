from django.db import models

class User(models.Model):
    usr_name = models.CharField(max_length=30)
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length=1)
    class Meta:
        db_table = 'user_tbl'

class Blogs(models.Model):
    usr_name = models.CharField(max_length=30)
    pst = models.TextField(max_length = 400)
    class Meta:
        db_table = 'blogs_tbl'