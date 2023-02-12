from django.urls import path

from content.views import IndexView, FoodView, Search, ReceiptsView, ReceiptDetailView


app_name = 'content'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('food/<int:category_id>', FoodView.as_view(), name='food'),
    path('search/', Search.as_view(), name='search'),
    path('receipts/<int:category_id>', ReceiptsView.as_view(), name='receipts'),
    path('receipt_detail/<int:pk>/', ReceiptDetailView.as_view(), name='receipt_detail'),
]