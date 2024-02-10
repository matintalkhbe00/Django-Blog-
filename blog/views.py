from django.shortcuts import render , get_object_or_404, redirect
from blog.models import Post, Category


# Create your views here.
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_details.html' , context={'post':post})

def posts_list(request):
    posts = Post.objects.all()
    # recent_posts = Post.objects.order_by('-create')[:3]
    return render(request , "blog/posts_list.html" , context={'posts':posts })

def categories_post(request , pk=None):
    category = get_object_or_404(Category, id=pk)
    posts = category.posts.all()
    return render(request , "blog/posts_list.html" , context={'posts':posts})