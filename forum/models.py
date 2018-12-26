from django.db import models

class Forum(models.Model):
    name = models.CharField(max_length=200)
    def __init__(self):
        pass

class Post(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# Create your models here.
