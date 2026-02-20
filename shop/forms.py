"""
Forms for CHANDRABHUSHAN ONLINE.
"""
from django import forms
from .models import Product, Inquiry, Service


class InquiryForm(forms.ModelForm):
    """Contact page inquiry form or service inquiry form."""
    class Meta:
        model = Inquiry
        fields = ['name', 'phone', 'email', 'message', 'related_service']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 4,
            }),
            'related_service': forms.HiddenInput(),  # Hidden field, set via URL parameter
        }


class ProductForm(forms.ModelForm):
    """Admin form for adding/editing products."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    """Admin form for adding/editing services/updates."""
    class Meta:
        model = Service
        fields = ['title', 'category', 'short_description', 'full_description', 
                  'required_documents', 'eligibility', 'start_date', 'end_date', 
                  'apply_link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'full_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'required_documents': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'List documents separated by commas or new lines'}),
            'eligibility': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'apply_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
