from . import views
from django.urls import path

urlpatterns = [
    path('cart', views.show_cart, name = 'cart'),
    path('add_to_cart',views.add_to_cart, name = 'add_to_cart'),
    path('remove_from_cart/<pk>',views.remove_from_cart, name = 'remove_from_cart'),
    path('checkout',views.checkout, name = 'checkout'),
    path('orders', views.orders, name = 'orders')
]