from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostManager(models.Manager):
    def counter_post(self):
        return len(self.all())

    def true_status_post(self):
        return len(self.all().filter(status=1))

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)     # unique_for_date='pub_date'
    body = models.TextField()
    img = models.ImageField(upload_to='post/' , null=True )
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    objects = models.Manager()
    costume_manager = PostManager()
    # pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'