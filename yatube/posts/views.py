from django.shortcuts import render, get_object_or_404

from .models import Post, Group

NUMBER_OF_POSTS_PER_PAGE = 10


def index(request):
    posts = Post.objects.select_related('author')[:NUMBER_OF_POSTS_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_OF_POSTS_PER_PAGE]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
