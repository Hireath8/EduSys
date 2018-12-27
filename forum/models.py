from django.db import models

char_max = 200

class TestUserForForum(models.Model):
    name = models.CharField(max_length=char_max)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class TestCourseForForum(models.Model):
    name = models.CharField(max_length=char_max)
    semester = models.CharField(max_length=char_max)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Forum(models.Model):
    name = models.CharField(max_length=char_max)
    creator = models.ForeignKey(TestUserForForum,on_delete=models.DO_NOTHING,related_name='forums_created')
    course = models.ForeignKey(TestCourseForForum,on_delete=models.CASCADE,related_name='forums_has')
    admins = models.ManyToManyField(TestUserForForum, related_name='forums_administrate')
    active = models.BooleanField()
    members = models.ManyToManyField(TestUserForForum, related_name='forums_belongs_to')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=char_max)
    # pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(TestUserForForum,on_delete=models.CASCADE, related_name='posts_has')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=char_max)
    # pub_date = models.DateTimeField('date published')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    at_users = models.ManyToManyField(TestUserForForum, related_name='comments_at')
    owner = models.ForeignKey(TestUserForForum,on_delete=models.CASCADE, related_name='comments_has')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


# Create your models here.
