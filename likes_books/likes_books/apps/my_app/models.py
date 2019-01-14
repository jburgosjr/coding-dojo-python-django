from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()
    uploader = models.ForeignKey(User, related_name = 'uploaded_books', on_delete = models.CASCADE)
    liked_users = models.ManyToManyField(User, related_name = 'liked_books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
