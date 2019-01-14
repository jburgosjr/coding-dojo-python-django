from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, related_name = 'written_books', on_delete = models.CASCADE)
    uploader = models.ForeignKey(User, related_name = 'uploaded_books', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name= 'written_reviews', on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
