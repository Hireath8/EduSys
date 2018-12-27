import string
import random
from forum.models import  *
def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def seed_string(value):
    if not value:
        value = random_string(10)
    return value


def seed_boolean(value):
    if not value:
        value = True
    return value

def add_forum_user(name=None):
    name = seed_string(name)
    user = TestUserForForum(name = name)
    user.save()
    return user

def add_forum_course(name=None, semester = None):
    name = seed_string(name)
    semester = seed_string(semester)
    course = TestCourseForForum(name=name,semester=semester)
    course.save()
    return course

def add_forum(user,course,name,admins,active,members):
    name = seed_string(name)
    active = seed_boolean(active)
    forum = Forum(name=name,creator=user,course=course,active=active)
    forum.save()
    forum.members.set(members)
    forum.admins.set(admins)
    return forum

def add_post(title,content,owner,forum):
    title = seed_string(title)
    content = seed_string(content)
    post = Post(title=title,owner=owner,forum=forum)
    post.save()
    comment = Comment(content=content,post=post,owner=owner)
    comment.save()
    return post

def add_post_with_comments(title,content,owner,replier,forum):
    title = seed_string(title)
    post = Post(title=title,owner=owner,forum=forum)
    post.save()
    content = seed_string(content)
    comment = Comment(content=content,post=post,owner=owner)
    comment.save()
    comment2 = Comment(content=content,post=post,owner=replier)
    comment2.save()
    comment3 = Comment(content=content,post=post,owner=owner)
    comment3.save()
    return post



def clear_all():
    Forum.objects.all().delete()
    TestCourseForForum.objects.all().delete()
    TestUserForForum.objects.all().delete()

def run_seeding():
    clear_all()
    david = add_forum_user('david')
    john = add_forum_user('john')
    amy = add_forum_user('amy')
    mary = add_forum_user('mary')
    math = add_forum_course('math','2018')
    science = add_forum_course('science','2018')
    math_forum = add_forum(david,math,'math-2018',[david,amy],True,[david,amy,john])
    science_forum = add_forum(david,science,'science-2018',[david,amy],True,[david,amy,mary])
    add_post(None,None,amy,math_forum)
    add_post(None,None,david,math_forum)
    add_post_with_comments(None,None,david,john,math_forum)