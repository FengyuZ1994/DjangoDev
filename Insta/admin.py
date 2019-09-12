from django.contrib import admin

from Insta.models import Post

# Register your models here.
# show the content defined in this app that should
# appear in admin's model
admin.site.register(Post)
# migration to make the change take effect
