from django.shortcuts import render

from .models import Post

# Create your views here.


def view_blog_post(request, slug_value):
    post = get_object_or_404(Post, slug=slug_value)
    return render(request, 'view_blog_post.html', locals())
