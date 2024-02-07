from django.shortcuts import render , get_object_or_404, redirect
from blog.models import Post
# Create your views here.
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_details.html' , context={'post':post})
