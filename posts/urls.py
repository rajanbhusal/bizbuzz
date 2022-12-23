from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('post/<str:pk>', views.viewPost, name="post"),
    path('create-post/', views.createPost, name="create-post"),
    path('delete-comment/<str:pk>', views.deleteComment, name="delete-comment"),
    path('delete-post/<str:pk>', views.deletePost, name="delete-post"),
    path('edit-comment/<str:pk>', views.editComment, name="edit-comment"),
    path('edit-post/<str:pk>', views.editPost, name="edit-post"),
    path('delete-like/<str:pk>', views.deleteLike, name="delete-like"),
    path('like-post/<str:pk>', views.likePost, name="like-post"),

]
