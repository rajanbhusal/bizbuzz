from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post, Comment, Like
from . forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . utils import searchPosts, paginatePages
# Create your views here.


def posts(request):
    search_query, posts = searchPosts(request)
    projects, page_obj = paginatePages(request, posts)
    context = {'posts': projects,
               'search_query': search_query, 'page_obj': page_obj}
    return render(request, 'posts/posts.html', context)


def viewPost(request, pk):
    postObj = Post.objects.get(id=pk)
    comments = postObj.comment_set.all()
    likes = postObj.like_set.all()
    likes_count = len(likes)
    liked_status = 'Like Post'
    for i in likes:
        if request.user.profile == i.liked_by:
            liked_status = 'Liked'

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user.profile
            comment.commented_post = postObj
            comment.save()
            messages.success(request, "You commented!")
            return redirect("post", pk=pk)
    context = {'post': postObj, 'comments': comments,
               'form': form, 'likes': likes_count, 'status': liked_status}
    return render(request, 'posts/post.html', context)


def deleteLike(request, pk):
    postObj = Post.objects.get(id=pk)
    likes = postObj.like_set.all()
    likes_count = len(likes)
    if likes_count > 0:
        likeObj = Like.objects.get(liked_by=request.user.profile,
                                   liked_post=postObj)
        likeObj.delete()
        messages.success(request, "Post Unliked!")
    return redirect('post', pk=pk)


def likePost(request, pk):
    postObj = Post.objects.get(id=pk)
    likes = postObj.like_set.all()
    likes_count = len(likes)
    liked_status = 'Like Post'
    for i in likes:
        if request.user.profile == i.liked_by:
            liked_status = 'Liked'
    if liked_status == 'Like Post':

        Like.objects.create(
            liked_by=request.user.profile,
            liked_post=postObj
        )
        messages.success(request, "Post liked!")
    return redirect('post', pk=pk)


def deleteComment(request, pk):
    commentObj = Comment.objects.get(id=pk)
    obj = 'comment'
    if commentObj:
        if request.method == 'POST':
            commentObj.delete()
            messages.success(request, "Comment deleted!")
            return redirect('post', pk=commentObj.commented_post.id)
    context = {'deleteObj': commentObj, 'obj': obj}
    return render(request, "posts/delete_form.html", context)


def editComment(request, pk):
    commentObj = Comment.objects.get(id=pk)
    form = CommentForm(instance=commentObj)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=commentObj)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            messages.success(request, "Comment Edited!")
            return redirect('post', pk=commentObj.commented_post.id)
    context = {'form': form}
    return render(request, "posts/edit_comment.html", context)


@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        if request.POST['description'] or request.FILES:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = request.user.profile
                post.save()
                messages.success(request, "Posted!")
                return redirect('posts')
            else:
                messages.error(request, "Form is not valid")
                return redirect('create-post')
        else:
            messages.error(request, "Empty Form cannot be submitted")
    context = {'form': form}
    return render(request, "posts/post_form.html", context)


def deletePost(request, pk):
    postObj = Post.objects.get(id=pk)
    obj = 'post'
    if postObj:
        if request.method == 'POST':
            postObj.delete()
            messages.success(request, "Post deleted!")
            return redirect('posts')
    context = {'deleteObj': postObj, 'obj': obj}
    return render(request, "posts/delete_form.html", context)


def editPost(request, pk):
    postObj = Post.objects.get(id=pk)
    form = PostForm(instance=postObj)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=postObj)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post edited!")
            return redirect('posts')
    context = {'form': form}
    return render(request, "posts/edit_post.html", context)
