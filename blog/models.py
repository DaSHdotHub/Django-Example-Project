from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Publish"))
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return self.title + ' | ' + str(self.author)
