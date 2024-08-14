from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:foo>', views.category, name='category'),
    path('all_products/', views.all_products, name='all_products'),
    path('sale_products/', views.sale_products, name='sale_products'),
    path('search/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
