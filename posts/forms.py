from django.forms import ModelForm
from . models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'post_image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description', 'comment_image']
