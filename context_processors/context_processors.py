from blog.models import Post

def recent_posts(requeset):
    recent_posts = Post.objects.order_by('-create')[:3]
    return {'recent_posts': recent_posts}