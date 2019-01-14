from django.db import models
    name = models.CharField(max_length = 160)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    books = models.ManyToManyField(Book, related_name = 'authors')
    notes = models.TextField()
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
