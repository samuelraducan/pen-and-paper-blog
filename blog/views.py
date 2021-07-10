from django.shortcuts import render
from .models import Post


# posts = [
#     {
#         'author': 'SamuelMBP',
#         'title': 'Blog Post No.1',
#         'content': 'First Post Content',
#         'date_posted': 'July 10, 2021'
#     },

#     {
#         'author': 'IlarialMBP',
#         'title': 'Blog Post No.2',
#         'content': 'Second Post Content',
#         'date_posted': 'August 11, 2021'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Pen & Paper About'})
