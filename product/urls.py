from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name = 'home'),
    path('products',views.products,name ='products'),
    path('product-details/<pk>',views.product_details,name='product_details')
]