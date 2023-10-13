from django.db import models
from django.contrib.auth.models import User
import math

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='image.jpg', blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    views = models.ManyToManyField(User, related_name='views', blank=True)
    saved = models.ManyToManyField(User, related_name='saved', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    comments_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:20] + '...'
    
    def time_to_read(self):
        return math.ceil(len(self.text.split(' ')) / 100)



class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_likes')
    comment_dislikes = models.ManyToManyField(User, related_name='comment_dislikes')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='reply')

    def __str__(self):
        return self.text
