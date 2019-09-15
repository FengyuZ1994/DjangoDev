from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Post(models.Model):
    # Django documentation: field options
    # title can be blank or no title
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True
    )
    def __str__(self):
        return self.title

    # auto-call this when creating a new post, search
    # name = 'post_detail' in urls.py and find its onw id
    def get_absolute_url(self):
        return reverse('post_detail', args = [str(self.id)])

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality':100},
        blank = True
    )
