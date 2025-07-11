from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('view-products/', views.product_list, name='view_products'),
    path('view-sales/', views.view_sales, name='view_sales'),

    # Changed from 'admin/' to 'custom-admin/'
    path('custom-admin/products/', views.product_list, name='product_list'),
    path('custom-admin/products/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('custom-admin/products/<int:pk>/view/', views.view_product, name='view_product'),
    path('custom-admin/products/<int:pk>/delete/', views.delete_product, name='delete_product'),
]

