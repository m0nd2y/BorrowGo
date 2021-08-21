from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length = 15, primary_key= True)
    user_pw = models.CharField(max_length = 15)
    user_name = models.CharField(max_length = 6)
    user_nickname = models.CharField(max_length = 10)
    user_school = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_phonenumber = models.CharField(max_length = 15)
    user_favorite = models.TextField()
    confirm = models.BooleanField(default=False)
