from django.contrib import admin

from Insta.models import Post, InstaUser

# Register your models here.
# show the content defined in this app that should
# appear in admin's model
admin.site.register(Post)
admin.site.register(InstaUser)
# migration to make the change take effect
