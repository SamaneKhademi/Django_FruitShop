from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:foo>', views.category, name='category'),
    path('all_products/', views.all_products, name='all_products'),
    path('sale_products/', views.sale_products, name='sale_products'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('update_info/', views.update_info, name='update_info'),
]
