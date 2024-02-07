from django.shortcuts import render
from blog.models import Post
from django.urls import reverse
# Create your views here.
def home(request):
    posts = Post.objects.all()
    post_recently = Post.objects.all()[:3]
    return render(request , 'home_app/home.html' , {'user' : request.user , 'posts' : posts , 'post_recently' : post_recently})