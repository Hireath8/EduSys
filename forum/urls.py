from django.urls import path

from . import views
app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:forum_id>/', views.detail, name='detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/create/', views.create_comment, name='create_comment'),
    path('post/<int:forum_id>/post/create', views.create_post, name='create_post'),
    path('create/', views.create_forum, name='create_forum'),


]
