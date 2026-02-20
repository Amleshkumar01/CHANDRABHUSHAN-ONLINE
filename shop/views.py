"""
Views for CHANDRABHUSHAN ONLINE - public pages and admin panel.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django import forms
from .models import Product, Inquiry, Service
from .forms import InquiryForm, ProductForm, ServiceForm


# ---------- Public Pages ----------

def home(request):
    """Home page with intro, banner offers, highlights - focused on online services."""
    services = Service.objects.all()[:6]
    return render(request, 'shop/home.html', {'services': services})


def about(request):
    """About Us page - shop history, owner, trust info."""
    return render(request, 'shop/about.html')


def product_list(request):
    """Products/Services page - list with images and price."""
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def product_detail(request, pk):
    """Single product detail view."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def gallery(request):
    """Gallery - shop and product images."""
    products = Product.objects.exclude(image='').exclude(image=None)
    return render(request, 'shop/gallery.html', {'products': products})


def contact(request):
    """Contact page with form, map, phone, email, WhatsApp."""
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            # Don't set related_service for general contact inquiries
            inquiry.related_service = None
            inquiry.save()
            messages.success(request, 'Thank you! Your message has been sent. We will contact you soon.')
            return redirect('shop:contact')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = InquiryForm()
        # Hide and make optional for general contact
        form.fields['related_service'].widget = forms.HiddenInput()
        form.fields['related_service'].required = False
    return render(request, 'shop/contact.html', {'form': form})


# ---------- Services & Latest Updates ----------

def service_list(request):
    """Services & Latest Updates listing page with category filter."""
    category = request.GET.get('category', '')
    services = Service.objects.all()
    
    if category:
        services = services.filter(category=category)
    
    categories = Service.CATEGORY_CHOICES
    return render(request, 'shop/services.html', {
        'services': services,
        'categories': categories,
        'selected_category': category,
    })


def service_detail(request, pk):
    """Service detail page with full information."""
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'shop/service_detail.html', {'service': service})


def service_inquiry(request, pk):
    """Inquiry form for a specific service - Contact to Fill Form."""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.related_service = service
            inquiry.save()
            messages.success(request, f'Thank you! Your inquiry for "{service.title}" has been submitted. We will contact you soon.')
            return redirect('shop:service_detail', pk=pk)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = InquiryForm(initial={'related_service': service})
        form.fields['related_service'].widget = forms.HiddenInput()
    return render(request, 'shop/service_inquiry.html', {'form': form, 'service': service})


# ---------- Admin Panel ----------

def admin_login_view(request):
    """Secure admin login."""
    if request.user.is_authenticated:
        return redirect('shop:admin_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome to the admin panel.')
            next_url = request.GET.get('next', 'shop:admin_dashboard')
            return redirect(next_url or 'shop:admin_dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'shop/admin/login.html')


def admin_logout_view(request):
    """Admin logout."""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('shop:home')


@login_required
def admin_dashboard(request):
    """Admin dashboard - overview and inquiries."""
    inquiries = Inquiry.objects.all()[:20]
    total_products = Product.objects.count()
    total_inquiries = Inquiry.objects.count()
    unread_inquiries = Inquiry.objects.filter(read=False).count()
    total_services = Service.objects.count()
    return render(request, 'shop/admin/dashboard.html', {
        'inquiries': inquiries,
        'total_products': total_products,
        'total_inquiries': total_inquiries,
        'unread_inquiries': unread_inquiries,
        'total_services': total_services,
    })


@login_required
def admin_inquiry_list(request):
    """View all customer inquiries."""
    inquiries = Inquiry.objects.all()
    return render(request, 'shop/admin/inquiry_list.html', {'inquiries': inquiries})


@login_required
def admin_inquiry_mark_read(request, pk):
    """Mark an inquiry as read."""
    inquiry = get_object_or_404(Inquiry, pk=pk)
    inquiry.read = True
    inquiry.save()
    messages.success(request, 'Marked as read.')
    return redirect('shop:admin_inquiry_list')


@login_required
def admin_product_list(request):
    """List all products for admin."""
    products = Product.objects.all()
    return render(request, 'shop/admin/product_list.html', {'products': products})


@login_required
def admin_product_add(request):
    """Add new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('shop:admin_product_list')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm()
    return render(request, 'shop/admin/product_form.html', {'form': form, 'title': 'Add Product'})


@login_required
def admin_product_edit(request, pk):
    """Edit product (name, description, price, image)."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('shop:admin_product_list')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/admin/product_form.html', {'form': form, 'product': product, 'title': 'Edit Product'})


@login_required
def admin_product_delete(request, pk):
    """Delete product."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('shop:admin_product_list')
    return render(request, 'shop/admin/product_confirm_delete.html', {'product': product})


# ---------- Admin: Services Management ----------

@login_required
def admin_service_list(request):
    """List all services for admin."""
    services = Service.objects.all()
    return render(request, 'shop/admin/service_list.html', {'services': services})


@login_required
def admin_service_add(request):
    """Add new service/update."""
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully.')
            return redirect('shop:admin_service_list')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceForm()
    return render(request, 'shop/admin/service_form.html', {'form': form, 'title': 'Add Service'})


@login_required
def admin_service_edit(request, pk):
    """Edit service (all fields)."""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('shop:admin_service_list')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'shop/admin/service_form.html', {'form': form, 'service': service, 'title': 'Edit Service'})


@login_required
def admin_service_delete(request, pk):
    """Delete service."""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted.')
        return redirect('shop:admin_service_list')
    return render(request, 'shop/admin/service_confirm_delete.html', {'service': service})
