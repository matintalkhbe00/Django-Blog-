from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(Post.objects.true_status_post() , Post.objects.counter_post())
    return render(request , 'home_app/home.html' , {'user' : request.user , 'posts' : posts})