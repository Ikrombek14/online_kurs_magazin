from django.urls import path
from .views import get_categories,update_product, get_details,delete_product, get_products,  add_product

urlpatterns = [
    path('', get_categories, name='get_categories'),
    path('products/<int:pk>', get_products, name='get_products'),
    path('products/details/<int:pk>', get_details, name='get_details'),
    path('add_product', add_product, name='add_product'),
    path('update_product/<int:pk>', update_product, name='update_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
]   