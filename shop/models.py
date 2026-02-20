"""
Database models for CHANDRABHUSHAN ONLINE.
"""
from django.db import models


class Product(models.Model):
    """Product/Service offered by the shop."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    """Customer inquiry/message from contact form or service inquiry."""
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    related_service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, 
                                         related_name='inquiries', help_text="Service/Job/Form this inquiry is about")
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        service_info = f" - {self.related_service.title}" if self.related_service else ""
        return f"{self.name}{service_info} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Service(models.Model):
    """Services & Latest Updates - Forms, Admit Cards, Jobs, Results."""
    CATEGORY_CHOICES = [
        ('Job', 'Job'),
        ('Admit Card', 'Admit Card'),
        ('Form', 'Form'),
        ('Result', 'Result'),
        ('Scholarship', 'Scholarship'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    short_description = models.TextField(max_length=300)
    full_description = models.TextField()
    required_documents = models.TextField(help_text="List documents separated by commas or new lines")
    eligibility = models.TextField(blank=True, help_text="Optional eligibility criteria")
    start_date = models.DateField()
    end_date = models.DateField()
    apply_link = models.URLField(blank=True, help_text="Official application link")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.category})"

    def is_active(self):
        """Check if service is currently active (between start and end date)."""
        from django.utils import timezone
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def is_expired(self):
        """Check if service has expired."""
        from django.utils import timezone
        today = timezone.now().date()
        return today > self.end_date
