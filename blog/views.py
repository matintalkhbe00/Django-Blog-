from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Comment
from django.core.paginator import Paginator


# Create your views here.


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('comment')
        Comment.objects.create(post=post, body=body, parent_id=parent_id, user=request.user)
    return render(request, 'blog/post_details.html', context={'post': post})


def posts_list(request):
    posts = Post.objects.all()
    # page_number = request.GET.get('page')
    # recent_posts = Post.objects.order_by('-create')[:3]
    paginator = Paginator(posts, 1)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, "blog/posts_list.html", context={'posts': object_list})


def categories_post(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    posts = category.posts.all()
    return render(request, "blog/posts_list.html", context={'posts': posts})


def search_post(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    paginator = Paginator(posts, 1)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, "blog/posts_list.html", context={'posts': object_list})