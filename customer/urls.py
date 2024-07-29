from . import views
from django.urls import path

urlpatterns = [
    path('account/', views.register_or_login, name = 'account'),
    path('logout/', views.sign_out, name = 'logout')
]