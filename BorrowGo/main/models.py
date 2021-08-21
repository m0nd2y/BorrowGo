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

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    writer_id = models.CharField(max_length = 10)
    post_title = models.CharField(max_length = 30)
    item = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    cost = models.IntegerField(null = True)
    post_content = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

class BorrowInfo(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    is_borrow = models.IntegerField(default=0) #0 : 대여 전, 1 : 대여 중, 2 : 대여 후 
    start_borrow = models.DateTimeField(null=True)
    end_borrow = models.DateTimeField(null=True)
    is_exceed = models.BooleanField(default=False)
    exceed_time = models.TimeField(null=True)
    exceed_cost = models.IntegerField(null=True)