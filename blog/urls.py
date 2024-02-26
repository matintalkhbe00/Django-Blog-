from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post_details/<slug:slug>', views.post_detail, name='post_data'),
    path('list/', views.posts_list, name='post_list'),
    path('categories/<int:pk>', views.categories_post, name='posts_categories'),
    path('search/', views.search_post, name='posts_search'),
    path('contactus/', views.contact_us, name='contact_us'),

]