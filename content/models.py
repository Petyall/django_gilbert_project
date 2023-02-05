from django.db import models


# Create your models here.
class FoodCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=128)
    permission = models.BooleanField()
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'еду'
        verbose_name_plural = 'Еда'

    def __str__(self):
        if self.permission:
            return f'{self.name} - можно'
        else:
            return f'{self.name} - нельзя'