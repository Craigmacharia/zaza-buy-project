from django.urls import path
from .api_views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('checkout/', CreateSaleView.as_view(), name='checkout'),
]
