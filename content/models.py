from django.db import models
from users.models import User


class FoodCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории еды'

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
        

class ReceiptCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории рецептов'

    def __str__(self):
        return self.name


class Receipt(models.Model):
    receipt_name = models.CharField(max_length=128)
    cooking_time = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='receipt_images', null=True, blank=True)
    category = models.ForeignKey(ReceiptCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    first_ingridient = models.CharField(max_length=64)
    second_ingridient = models.CharField(max_length=64)
    third_ingridient = models.CharField(max_length=64, null=True, blank=True)
    fourth_ingridient = models.CharField(max_length=64, null=True, blank=True)
    fifth_ingridient = models.CharField(max_length=64, null=True, blank=True)
    sixth_ingridient = models.CharField(max_length=64, null=True, blank=True)
    seventh_ingridient = models.CharField(max_length=64, null=True, blank=True)
    eighth_ingridient = models.CharField(max_length=64, null=True, blank=True)
    nineth_ingridient = models.CharField(max_length=64, null=True, blank=True)
    tenth_ingridient = models.CharField(max_length=64, null=True, blank=True)

    first_step = models.TextField()
    second_step = models.TextField()
    third_step = models.TextField(null=True, blank=True)
    fourth_step = models.TextField(null=True, blank=True)
    fifth_step = models.TextField(null=True, blank=True)
    sixth_step = models.TextField(null=True, blank=True)
    seventh_step = models.TextField(null=True, blank=True)
    eighth_step = models.TextField(null=True, blank=True)
    nineth_step = models.TextField(null=True, blank=True)
    tenth_step = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепт'

    def __str__(self):
        return self.receipt_name