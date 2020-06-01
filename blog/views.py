from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Tim Park',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 29, 2018'
    }
]


def home(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request, *args, **kwargs):
    return render(request, 'blog/about.html', {'title': 'About'})
