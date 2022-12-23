from . models import Post
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger


def searchPosts(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    posts = Post.objects.distinct().filter(
        Q(owner__name__icontains=search_query) |
        Q(description__icontains=search_query)
    )
    return search_query, posts


def paginatePages(request, posts):
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        projects = paginator.page(page_number)
    return projects, page_obj
