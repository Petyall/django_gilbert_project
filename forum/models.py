from django.db import models
from users.models import User

class PostCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории постов'

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Пост'

    def __str__(self):
        return self.name

class PostCommentary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    description = models.TextField()   
    date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} - {self.post} - {self.date}'