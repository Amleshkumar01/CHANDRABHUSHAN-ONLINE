"""
Django admin registration for shop models.
"""
from django.contrib import admin
from .models import Product, Inquiry, Service


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_date']
    search_fields = ['name', 'description']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'related_service', 'created_at', 'read']
    list_filter = ['read', 'created_at', 'related_service']
    search_fields = ['name', 'phone', 'email', 'message']
    date_hierarchy = 'created_at'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_date', 'end_date', 'created_at']
    list_filter = ['category', 'start_date', 'end_date']
    search_fields = ['title', 'short_description', 'full_description']
    date_hierarchy = 'created_at'
