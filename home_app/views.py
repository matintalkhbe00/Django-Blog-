from django.shortcuts import render
from blog.models import Post
from django.urls import reverse


# Create your views here.
def home(request):
    posts = Post.objects.all()
    post_recently = Post.objects.all()[:3]
    posts_show = Post.objects.all().order_by('-create')[:3]
    return render(request,
                  'home_app/home.html',
                  {
                      'user': request.user,
                      'posts': posts,
                      'post_recently': post_recently,
                      'posts_show': posts_show})


# we can use ("django render partial") library for address (more information "https://pypi.org/project/django-render-partial/")
