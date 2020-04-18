from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import datetime
# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    publish = models.DateTimeField(default=datetime.datetime.now, blank=True)
    img = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):  # new
        return reverse('detail', args=[str(self.slug)])
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     body = models.TextField()

#     def __str__(self):
#         return self.title
