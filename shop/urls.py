"""
URL configuration for shop app - CHANDRABHUSHAN ONLINE.
"""
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    # Services & Latest Updates
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/<int:pk>/inquiry/', views.service_inquiry, name='service_inquiry'),
    # Admin
    path('admin-panel/login/', views.admin_login_view, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout_view, name='admin_logout'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/inquiries/', views.admin_inquiry_list, name='admin_inquiry_list'),
    path('admin-panel/inquiries/<int:pk>/read/', views.admin_inquiry_mark_read, name='admin_inquiry_mark_read'),
    path('admin-panel/products/', views.admin_product_list, name='admin_product_list'),
    path('admin-panel/products/add/', views.admin_product_add, name='admin_product_add'),
    path('admin-panel/products/<int:pk>/edit/', views.admin_product_edit, name='admin_product_edit'),
    path('admin-panel/products/<int:pk>/delete/', views.admin_product_delete, name='admin_product_delete'),
    # Admin: Services
    path('admin-panel/services/', views.admin_service_list, name='admin_service_list'),
    path('admin-panel/services/add/', views.admin_service_add, name='admin_service_add'),
    path('admin-panel/services/<int:pk>/edit/', views.admin_service_edit, name='admin_service_edit'),
    path('admin-panel/services/<int:pk>/delete/', views.admin_service_delete, name='admin_service_delete'),
]
