from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse
from forum.models import *
from django.template import loader
from forum.utls import extract_at_users
# def index(request):
#     return HttpResponse("Hello You're at the forum index.")



def index(request):
    forums = Forum.objects.all()
    template = loader.get_template('index.html')
    context = {'forums':forums}
    return HttpResponse(template.render(context, request))


def get_edit_forum(request,forum_id):
    pass

def get_create_forum(request):

    pass

def detail(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    print(forum.name)
    template = loader.get_template('detail.html')
    context = {'forum': forum,'posts':forum.post_set.all()}
    return HttpResponse(template.render(context, request))

def post_forum(request,forum_id):
    pass

def create_forum(request):
    course_name = request.POST['course_name']
    name = request.POST['name']
    owner = TestUserForForum.objects.all()[0]
    forum = Forum(name=name, creator=owner,course=TestCourseForForum.objects.get(name=course_name),active=True)
    forum.save()
    return redirect('forum:index')

def delete_forum(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    if forum.delete():
        return redirect('forum:index')
    else:
        pass


def get_create_post(request, post_id):
    pass


def post_detail(request, post_id):
    template = loader.get_template('post_detail.html')
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()
    context = {'post':post,'comments':comments}
    return HttpResponse(template.render(context, request))



def delete_post(request, post_id):
    pass

def create_post(request, forum_id):
    title = request.POST['title']
    content = request.POST['content']
    owner = TestUserForForum.objects.all()[0]
    post = Post(title=title, owner=owner, forum_id=forum_id)
    post.save()
    comment = Comment(content=content, post=post, owner=owner)
    comment.save()
    return redirect('forum:post_detail',post_id=post.id)


def get_comment(request,comment_id):
    pass

def get_edit_comment(request,comment_id):
    pass

def post_comment(request,comment_id):
    pass

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    pass


def create_comment(request,post_id):
    owner = TestUserForForum.objects.all()[0]
    post = get_object_or_404(Post, id=post_id)
    content = request.POST['content']
    comment = Comment(content=content, owner=owner, post=post)
    comment.save()
    user_names = extract_at_users(content)
    users = []
    for user_name in user_names:
        user = TestUserForForum.objects.get(name=user_name)
        users.append(user)
    comment.at_users.set(users)
    template = loader.get_template('post_detail.html')
    comments = post.comment_set.all()
    context = {'post': post, 'comments': comments}
    return redirect('forum:post_detail', post_id=post_id)