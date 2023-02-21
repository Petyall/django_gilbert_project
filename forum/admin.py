from django.contrib import admin
from forum.models import Post, PostCategory, PostCommentary
# Register your models here.
admin.site.register(PostCommentary)
admin.site.register(Post)
admin.site.register(PostCategory)