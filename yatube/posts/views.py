from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):    
    posts = Post.objects.select_related('author')[:10]
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/index.html', context) 

def post(request):    
    template = 'posts/group_list.html'
    return render(request, template)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('group')[:10]
    template = 'posts/group_list.html'
    text = 'Записи сообщества'
    context = {
        'group': group,
        'posts': posts,
        'text': text
    }
    return render(request, template, context)
