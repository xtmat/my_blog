from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=260)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.localtime)
    published_date = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(max_length = 200,null = True,blank = True)

    def publish(self):
        self.published_date = timezone.localtime() ####################biggest but
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.localtime)  ####################


    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
