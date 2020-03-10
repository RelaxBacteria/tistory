from django.db import models
from helpers.models import BaseModel
from users.models import User

from taggit.managers import TaggableManager

# Create your models here.

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)
    tags = TaggableManager()

    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.user) + str(self.title)

    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name = "게시물"
        verbose_name_plural = "게시물"

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.user) + str(self.content)