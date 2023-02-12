from django.contrib import admin
from content.models import Food, FoodCategory, ReceiptCategory, Receipt


admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(ReceiptCategory)

@admin.register(Receipt)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('receipt_name', 'category')
    fields = ('receipt_name', 'category', 'cooking_time', 'description', 'author', 'image', 
              ('first_ingridient', 'second_ingridient'),
              ('third_ingridient', 'fourth_ingridient'),
              ('fifth_ingridient', 'sixth_ingridient'),
              ('seventh_ingridient', 'eighth_ingridient'),
              ('nineth_ingridient', 'tenth_ingridient'),
              'first_step', 'second_step',
              'third_step', 'fourth_step',
              'fifth_step', 'sixth_step',
              'seventh_step', 'eighth_step',
              'nineth_step', 'tenth_step',
            )
    search_fields = ('receipt_name',)
    ordering = ('receipt_name',)