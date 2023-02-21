from django.urls import path

from forum.views import HomeView, PostDetailView, Search


app_name = 'forum'

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    # path('food/<int:category_id>', FoodView.as_view(), name='food'),
    path('search/', Search.as_view(), name='search'),
    # path('receipts/<int:category_id>', ReceiptsView.as_view(), name='receipts'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]