from django.db import models
from django.urls import reverse
from django.utils import timezone
from .managers import PublishedManager

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,default='published')
    
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('main:post_detail',
                       args=[self.publish.year,
                            self.publish.month,
                            self.publish.day, 
                            self.slug])

class Comment(models.Model):
    post = models. ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models. EmailField()
    body = models. TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


    def __str__(self):
        return f'Comment by {self.name} on {self.post}'