from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True)

class Description(models.Model):
    desc = models.TextField()
    courses = models.OneToOneField(Course, on_delete = models.CASCADE, primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True) 

class Comment(models.Model):
     comment = models.TextField()
     courses_comment = models.ForeignKey(Course, related_name = 'comments', on_delete = models.CASCADE)
     created_at = models.DateTimeField(auto_now_add = True)
     updated_at= models.DateTimeField(auto_now = True) 

