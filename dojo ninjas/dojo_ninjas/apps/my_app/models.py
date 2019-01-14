from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 60)
    city = models.CharField(max_length = 60)
    state = models.CharField(max_length = 60)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ninja(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    enroled = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    