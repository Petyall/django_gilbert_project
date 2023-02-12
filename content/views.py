from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from content.models import Food, FoodCategory, Receipt, ReceiptCategory


class IndexView(TemplateView):
    template_name = 'content/index.html'


class FoodView(ListView):
    template_name = 'content/food.html'
    model = Food

    def get_queryset(self):
        queryset = super(FoodView, self).get_queryset()
        category_id = self.kwargs.get('category_id') #  category_id передается из urls.py
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self):
        # super(FoodView, self) - кусок ООП, нужный для сохранения функционала метода родительского класса, так как он был переделан
        # Иными словами, сначала передаем родителя (FoodView), сохраняем все его функции, а затем добавляем новые.
        context = super(FoodView, self).get_context_data()
        # Передача категорий товаров в context
        context['categories'] = FoodCategory.objects.all()
        return context
    

class Search(ListView):
    template_name = 'content/food.html'
    model = Food

    def get_queryset(self, **kwargs):
        return Food.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    

class ReceiptsView(ListView):
    template_name = 'content/receipts.html'
    model = Receipt
    paginate_by = 2

    def get_queryset(self):
        queryset = super(ReceiptsView, self).get_queryset()
        category_id = self.kwargs.get('category_id') #  category_id передается из urls.py
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self):
        # super(FoodView, self) - кусок ООП, нужный для сохранения функционала метода родительского класса, так как он был переделан
        # Иными словами, сначала передаем родителя (FoodView), сохраняем все его функции, а затем добавляем новые.
        context = super(ReceiptsView, self).get_context_data()
        # Передача категорий товаров в context
        context['categories'] = ReceiptCategory.objects.all()
        return context
    

class ReceiptDetailView(DetailView):
    model = Receipt
    template_name = 'content/receipt_detail.html'