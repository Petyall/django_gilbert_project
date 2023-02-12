from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_verified_email = models.BooleanField(default=False)


class UsersReceipts(models.Model):
    receipt_name = models.CharField(max_length=128)
    cooking_time = models.CharField(max_length=32)
    image = models.ImageField(upload_to='users_receipt_images', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=128, null=True, blank=True)
    steps = models.TextField()

    def __str__(self):
        return self.receipt_name