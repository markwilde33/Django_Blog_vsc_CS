from django.shortcuts import render

# Create your views here.

posts = [

    {

        'author': 'sparks',
        'title': 'Blog Post 1',
        'content': 'Pish',
        'date_posted': 'December 12, 3939',
        'ps': 'Keep fighting'

    },

    {

        'author': 'muffy',
        'title': 'Blog Post 2',
        'content': 'Sham',
        'date_posted': 'November 25, 4000',
        'ps': 'no reteat no surrender'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
